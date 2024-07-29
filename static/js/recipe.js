const editButtons = document.getElementsByClassName("recipe-btn-edit");

const recipeTitle = document.getElementById("id_title");
const recipeCategory = document.getElementById("id_category");
const recipeFeatured_image = document.getElementById("id_featured_image");
const recipeDescription = document.getElementById("id_description");
const recipeIngredients = document.getElementById("id_ingredients");
const recipeInstructions = document.getElementById("id_instructions");
const recipeStatus = document.getElementById("id_status");

const recipeForm = document.getElementById("recipeForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let recipeId = e.target.getAttribute("data-recipe-id");
        let recipeContent = document.getElementById(`recipe${recipeId}`).innerText;
        recipeTitle.value = recipeContent;
        submitButton.innerText = "Update";
        recipeForm.setAttribute("action", `edit_recipe/${recipeId}/`);
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let recipeId = e.target.getAttribute("data-recipe-id");
        deleteConfirm.href = `delete_recipe/${recipeId}/`;
        deleteModal.show();
    });
}
