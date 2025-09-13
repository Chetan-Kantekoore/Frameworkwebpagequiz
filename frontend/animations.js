// animations.js

/**
 * Animate a card with smooth entry effect
 * @param {HTMLElement} card 
 */
export function animateCard(card) {
    if (!card) return;
    card.classList.add("animate-card");
    setTimeout(() => {
        card.classList.remove("animate-card");
    }, 800); // slightly longer for smoother feel
}

/**
 * Add hover and focus effects to options
 * @param {NodeListOf<HTMLElement>} optionLabels 
 */
export function optionHoverEffect(optionLabels) {
    optionLabels.forEach(label => {
        // Hover animation
        label.addEventListener("mouseenter", () => {
            label.style.transition = "transform 0.25s ease, box-shadow 0.25s ease";
            label.style.transform = "scale(1.05)";
            label.style.boxShadow = "0 6px 18px rgba(0,0,0,0.12)";
        });

        // Reset on leave
        label.addEventListener("mouseleave", () => {
            label.style.transform = "scale(1)";
            label.style.boxShadow = "none";
        });

        // Keyboard accessibility (focus/blur)
        label.addEventListener("focus", () => {
            label.style.outline = "3px solid #6366f1";
            label.style.outlineOffset = "3px";
        });
        label.addEventListener("blur", () => {
            label.style.outline = "none";
        });
    });
}

/**
 * Add subtle click feedback (press effect)
 * @param {NodeListOf<HTMLElement>} optionLabels 
 */
export function optionClickEffect(optionLabels) {
    optionLabels.forEach(label => {
        label.addEventListener("mousedown", () => {
            label.style.transform = "scale(0.97)";
        });
        label.addEventListener("mouseup", () => {
            label.style.transform = "scale(1.05)";
        });
    });
}
