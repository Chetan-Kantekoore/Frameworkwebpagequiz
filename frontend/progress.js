// progress.js
export function updateProgress(progressBar, progressText, percentage) {
    progressBar.style.width = "0%";
    setTimeout(() => {
        progressBar.style.width = percentage + "%";
        progressText.textContent = percentage + "%";
    }, 100);
}
