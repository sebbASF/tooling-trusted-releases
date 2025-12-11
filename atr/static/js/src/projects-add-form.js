document.addEventListener("DOMContentLoaded", () => {
	const configElement = document.getElementById("projects-add-config");
	if (!configElement) return;

	const committeeDisplayName = configElement.dataset.committeeDisplayName;
	const committeeName = configElement.dataset.committeeName;
	if (!committeeDisplayName || !committeeName) return;

	const formTexts = document.querySelectorAll(".form-text, .text-muted");
	formTexts.forEach((element) => {
		element.textContent = element.textContent.replaceAll(
			"Example",
			committeeDisplayName,
		);
		element.textContent = element.textContent.replaceAll(
			"example",
			committeeName.toLowerCase(),
		);
	});
});
