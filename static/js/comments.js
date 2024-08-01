/* jshint esversion: 6 */
/* global bootstrap */

document.addEventListener('DOMContentLoaded', function() {
    // Get elements related to editing comments
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    // Initialize Bootstrap modal for deleting comments
    const deleteModalElement = document.getElementById("deleteModal");
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    // Check if all required elements exist
    if (deleteModalElement && deleteButtons.length && editButtons.length && commentText && commentForm && submitButton && deleteConfirm) {
        const deleteModal = new bootstrap.Modal(deleteModalElement);

        // Add event listeners to all edit buttons
        for (let button of editButtons) {
            button.addEventListener("click", (e) => {
                // Get the comment ID from the button's data attribute
                let commentId = e.target.getAttribute("data-comment-id");
                // Get the current content of the comment
                let commentContent = document.getElementById(`comment${commentId}`).innerText;
                // Set the comment text area with the current comment content
                commentText.value = commentContent;
                // Change the submit button text to "Update"
                submitButton.innerText = "Update";
                // Update the form action to the edit URL for the specific comment
                commentForm.setAttribute("action", `edit_comment/${commentId}/`);
            });
        }

        // Add event listeners to all delete buttons
        for (let button of deleteButtons) {
            button.addEventListener("click", (e) => {
                // Get the comment ID from the button's data attribute
                let commentId = e.target.getAttribute("data-comment-id");
                // Update the confirm delete link with the URL for the specific comment
                deleteConfirm.href = `delete_comment/${commentId}/`;
                // Show the delete confirmation modal
                deleteModal.show();
            });
        }
    } else {
        console.error("Some required elements are missing in the DOM. In some case It's ok");
    }
});
