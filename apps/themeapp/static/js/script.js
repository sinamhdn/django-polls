const choiceForms = document.querySelectorAll(".choice-form");
const choiceFormContainer = document.querySelector(".choice-form-container");
const addButton = document.querySelector("#add-choice");
const totalForms = document.querySelector("#id_choice_set-TOTAL_FORMS");

let lastFormNumber = choiceForms.length - 1;

if (addButton) {
  addButton.addEventListener("click", (e) => {
    e.preventDefault();
    console.log("clicked");
    //   clone the choice form
    const newForm = choiceForms[0].cloneNode(true);
    //Regex to find all instances of the form number
    const formRegex = RegExp(`choice_set-(\\d){1}-`, "g");
    //Increment the form number
    lastFormNumber = lastFormNumber + 1;
    //Update the new form to have the correct form number
    newForm.innerHTML = newForm.innerHTML.replace(
      formRegex,
      `choice_set-${lastFormNumber}-`
    );
    //Insert the new form at the end of the list of forms
    choiceFormContainer.insertBefore(newForm, addButton);
    //Increment the number of total forms in the management form
    totalForms.setAttribute("value", `${lastFormNumber + 1}`);
  });
}
