// static/js/upload.js

let dropZone = document.getElementById("dropZone");
let fileInput = document.getElementById("fileInput");
let uploadForm = document.getElementById("uploadForm");
let loadingIndicator = document.getElementById("loadingIndicator");

if (dropZone) {
    dropZone.addEventListener("click", function () {
        fileInput.click();
    });

    fileInput.addEventListener("click", function (event) {
        event.stopPropagation();
    });

    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            showLoadingState();
            uploadForm.submit();
        }
    });

    dropZone.addEventListener("dragover", function (event) {
        event.preventDefault();
        event.stopPropagation();
        this.classList.add("dragover");
    });

    dropZone.addEventListener("dragleave", function (event) {
        event.preventDefault();
        event.stopPropagation();
        this.classList.remove("dragover");
    });

    dropZone.addEventListener("drop", function (event) {
        event.preventDefault();
        event.stopPropagation();
        this.classList.remove("dragover");

        let file = event.dataTransfer.files[0];
        fileInput.files = event.dataTransfer.files;
        showLoadingState();
        uploadForm.submit();
    });
}

function showLoadingState() {
    loadingIndicator.style.display = 'block';
}

function hideLoadingState() {
    loadingIndicator.style.display = 'none';
}

window.addEventListener("load", function () {
    hideLoadingState();
});
