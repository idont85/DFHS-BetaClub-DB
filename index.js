const hiddenInput = document.getElementById('scannerInput');
var currentString = '';

const errorAudio = new Audio("/assets/sounds/error.mp3")
errorAudio.volume = 1;

const acceptedAudio = new Audio("/assets/sounds/accepted.mp3")
acceptedAudio.volume = 1;

function manualRefocus() {
    console.log("Refocused Input")
    hiddenInput.focus();
}

document.addEventListener('DOMContentLoaded', () => {
    const firebaseConfig = {
        apiKey: "AIzaSyAnazpO3yaePD2KcJ2PAXxmoEXGp7KcXT4",
        authDomain: "betasignin-a8249.firebaseapp.com",
        projectId: "betasignin-a8249",
        storageBucket: "betasignin-a8249.appspot.com",
        messagingSenderId: "313701535965",
        appId: "1:313701535965:web:ecc487e3543034a369cb34",
        measurementId: "G-F2XGH39WEZ"
    };

    const app = firebase.initializeApp(firebaseConfig);
    const db = firebase.firestore();

    const table = document.querySelector('.mainLoggingTable');
    const tableContainer = document.querySelector('.tableContainer');
    let studentNames = {};
    let studentStatuses = {};

    fetch('/databases/studentNames.json')
        .then(response => response.json())
        .then(data => {
            studentNames = data;
        });

    fetch('/databases/studentStatus.json')
        .then(response => response.json())
        .then(data => {
            studentStatuses = data;
        });

    hiddenInput.focus();

    document.addEventListener('keydown', (event) => {
        currentString += event.key
        if (event.key >= '0' && event.key <= '9') {
            hiddenInput.focus();
        }
    });

    hiddenInput.addEventListener('input', function () {
        if (this.value.length === 5) {
            console.log(currentString)
            currentString = '';
            const studentId = this.value;
            const studentName = studentNames[studentId] || "Unknown";
            let studentStatus = studentStatuses[studentId] || "Unknown";

            if (studentStatus === "true") {
                studentStatus = "Paid";
            } else if (studentStatus === "false") {
                studentStatus = "Not Paid";
            } else {
                studentStatus = "Unknown";
                
            }

            const existingRow = findRowById(studentId);
            if (existingRow) {
                updateRepeatedCount(existingRow);
                const repeatedCount = existingRow.cells[0].textContent;
                updateFirestore(studentId, repeatedCount, studentName, studentStatus);
                if (repeatedCount > 0) {
                    errorAudio.play()
                    setTimeout(() => {
                        alert("⚠️ Warning! This ID has already been scanned! ⚠️")
                    }, 100);
                    
                }
            } else if (studentName == "Unknown") {
                errorAudio.play()
                setTimeout(() => {
                    alert("⚠️ Warning! Could not find student associated with ID! ⚠️")
                }, 100);
                addRow(studentId, studentName, studentStatus);
                saveToFirestore(studentId, studentName, studentStatus, 1); 
            } else {
                acceptedAudio.play()
                addRow(studentId, studentName, studentStatus);
                saveToFirestore(studentId, studentName, studentStatus, 1); 
            }

            if (studentStatus === "true") {
                showCheckmark('#yes');
            } else if (studentStatus === "false") {
                showCheckmark('#no');
            } else {
                showCheckmark('#neutral');
            }

            this.value = '';
            hiddenInput.focus();
            scrollToBottom();
        }
    });

    function showCheckmark(selector) {
        const checkmark = document.querySelector(selector);
        checkmark.style.display = 'block';
        setTimeout(() => {
            checkmark.style.display = 'none';
        }, 1500);
    }

    function scrollToBottom() {
        tableContainer.scrollTop = tableContainer.scrollHeight;
    }

    function findRowById(studentId) {
        const rows = table.querySelectorAll('tr:not(:first-child)');
        for (const row of rows) {
            if (row.cells[1].textContent === studentId) {
                return row;
            }
        }
        return null;
    }

    function updateRepeatedCount(row) {
        const matchesCell = row.cells[0];
        let repeatedCount = parseInt(matchesCell.textContent, 10) || 0;
        matchesCell.textContent = repeatedCount + 1;
/*         if (repeatedCount > 0) {
          alert("⚠️ Warning! This ID has already been scanned! ⚠️")
        } */
    }

    function addRow(studentId, studentName, studentStatus, repeated = 1, time = new Date().toLocaleTimeString()) {
        const newRow = document.createElement('tr');

        const matchesCell = document.createElement('td');
        matchesCell.textContent = repeated;
        newRow.appendChild(matchesCell);

        const idCell = document.createElement('td');
        idCell.textContent = studentId;
        newRow.appendChild(idCell);

        const nameCell = document.createElement('td');
        nameCell.textContent = studentName;
        newRow.appendChild(nameCell);

        const statusCell = document.createElement('td');
        statusCell.textContent = studentStatus;
        newRow.appendChild(statusCell);

        const timeCell = document.createElement('td');
        timeCell.textContent = time;
        newRow.appendChild(timeCell);

        table.appendChild(newRow);
    }

    function saveToFirestore(studentId, studentName, studentStatus, repeatedCount) {
        const time = new Date().toLocaleTimeString();
        db.collection('students').add({
            studentId: studentId,
            studentName: studentName,
            studentStatus: studentStatus,
            repeatedCount: repeatedCount,
            timeLogged: time
        });
    }

    function updateFirestore(studentId, repeatedCount, studentName, studentStatus) {
        db.collection('students').where('studentId', '==', studentId)
            .get()
            .then(querySnapshot => {
                querySnapshot.forEach(doc => {
                    db.collection('students').doc(doc.id).update({
                        repeatedCount: repeatedCount,
                        studentName: studentName,
                        studentStatus: studentStatus
                    });
                });
            });
    }

    function loadFromFirestore() {
        db.collection('students')
            .orderBy('timeLogged', 'asc')
            .get()
            .then((querySnapshot) => {
                querySnapshot.forEach((doc) => {
                    const data = doc.data();
                    addRow(data.studentId, data.studentName, data.studentStatus, data.repeatedCount, data.timeLogged);
                });
            });
    }

    loadFromFirestore();
});

/* Formatted using Precise */