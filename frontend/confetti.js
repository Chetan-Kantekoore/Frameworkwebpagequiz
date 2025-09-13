// confetti.js
export function launchConfetti() {
    confetti({
        particleCount: 200,
        spread: 150,
        origin: { y: 0.6 },
        colors: ['#ff0a54','#ff477e','#ff7096','#ff85a1','#fbb1b1','#f9bec7']
    });
}
