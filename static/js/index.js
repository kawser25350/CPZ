document.addEventListener("DOMContentLoaded", () => {
	/* ==================================================
	   HOME PAGE MAIN: templates/pages/home.html
	   Adds a staggered reveal effect to elements using
	   the .reveal-on-load class.
	   ================================================== */
	const revealItems = document.querySelectorAll(".reveal-on-load");

	revealItems.forEach((item, index) => {
		window.setTimeout(() => {
			item.classList.add("is-visible");
		}, 120 * index);
	});

	/* ==================================================
	   POST MODAL: Open full post content on read article click
	   ================================================== */
	const postModal = document.getElementById("post-modal");
	const modalClose = document.querySelector(".post-modal__close");
	const modalBackdrop = document.querySelector(".post-modal__backdrop");
	const postLinks = document.querySelectorAll(".post-link");

	if (postLinks.length > 0) {
		postLinks.forEach((link) => {
			link.addEventListener("click", (e) => {
				e.preventDefault();
				const postId = link.getAttribute("data-post-id");
				const postCard = document.querySelector(`[data-post-id="${postId}"]`);
				
				if (postCard) {
					const title = postCard.getAttribute("data-post-title");
					const fullContent = postCard.getAttribute("data-post-content");
					const author = postCard.getAttribute("data-post-author");
					
					document.querySelector(".post-full__title").textContent = title;
					document.querySelector(".post-full__meta").innerHTML = `<small>By <strong>${author}</strong></small>`;
					document.querySelector(".post-full__content").textContent = fullContent;
					
					postModal.classList.add("is-open");
					document.body.style.overflow = "hidden";
				}
			});
		});
	}

	const closeModal = () => {
		postModal.classList.remove("is-open");
		document.body.style.overflow = "auto";
	};

	if (modalClose) modalClose.addEventListener("click", closeModal);
	if (modalBackdrop) modalBackdrop.addEventListener("click", closeModal);
	document.addEventListener("keydown", (e) => {
		if (postModal && e.key === "Escape" && postModal.classList.contains("is-open")) {
			closeModal();
		}
	});

	/* ==================================================
	   HOME POST CARD: Show more / Show less toggle
	   Syncs button label and preview visibility.
	   ================================================== */
	const postToggleButtons = document.querySelectorAll(".post-toggle-btn");

	postToggleButtons.forEach((button) => {
		const targetSelector = button.getAttribute("data-bs-target");
		const previewId = button.getAttribute("data-preview-id");
		const collapseEl = targetSelector ? document.querySelector(targetSelector) : null;
		const previewEl = previewId ? document.getElementById(previewId) : null;

		if (!collapseEl) return;

		collapseEl.addEventListener("show.bs.collapse", () => {
			button.textContent = "Show less";
			if (previewEl) previewEl.style.display = "none";
		});

		collapseEl.addEventListener("hide.bs.collapse", () => {
			button.textContent = "Show more";
			if (previewEl) previewEl.style.display = "block";
		});
	});
});
