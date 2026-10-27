document.querySelectorAll("[data-share]").forEach((button) => {
    button.addEventListener("click", async () => {
        const url = new URL(button.dataset.shareUrl || window.location.href, window.location.href).href;
        const title = button.dataset.shareTitle || document.title;
        const text = button.dataset.shareText || "";
        const status = document.querySelector("[data-share-status]");

        if (navigator.share) {
            try {
                await navigator.share({ title, text, url });
                if (status) status.textContent = "Share options opened.";
                return;
            } catch (error) {
                if (error.name === "AbortError") return;
            }
        }

        try {
            await navigator.clipboard.writeText(url);
            if (status) status.textContent = "Link copied. Paste it into WhatsApp, X, LinkedIn, or another app.";
        } catch {
            if (status) status.textContent = `Sharing is unavailable here. Copy this link manually: ${url}`;
        }
    });
});
