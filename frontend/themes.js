// themes.js
export function setTheme(themeColor) {
    document.body.style.background = themeColor;
    document.querySelectorAll(".quiz-card").forEach(card => {
        card.style.background = themeColor;
    });
}
