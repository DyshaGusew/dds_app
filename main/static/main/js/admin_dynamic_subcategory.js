document.addEventListener("DOMContentLoaded", function () {
    const categorySelect = document.getElementById("id_category");
    const subCategorySelect = document.getElementById("id_sub_category");

    if (!categorySelect || !subCategorySelect) return;

    // Сохраняем текущую выбранную подкатегорию (если редактируем запись)
    const initialSubCategory = subCategorySelect.value;

    function updateSubCategories() {
        const categoryId = categorySelect.value;

        // Очистка подкатегорий
        subCategorySelect.innerHTML = "";
        const emptyOption = document.createElement("option");
        emptyOption.value = "";
        emptyOption.textContent = "---------";
        subCategorySelect.appendChild(emptyOption);

        if (!categoryId) return;

        // AJAX запрос к серверу
        const xhr = new XMLHttpRequest();
        xhr.open("GET", `/admin/main/ddsrecord/get_subcategories/?category_id=${encodeURIComponent(categoryId)}`);
        xhr.responseType = "json";
        xhr.onload = function () {
            if (xhr.status === 200 && Array.isArray(xhr.response.subcategories)) {
                xhr.response.subcategories.forEach(function (subcat) {
                    const option = document.createElement("option");
                    option.value = subcat.id;
                    option.textContent = subcat.name;
                    if (String(subcat.id) === String(initialSubCategory)) {
                        option.selected = true;
                    }
                    subCategorySelect.appendChild(option);
                });
            } else {
                console.error("Ошибка загрузки подкатегорий", xhr.response);
            }
        };
        xhr.onerror = function () {
            console.error("Ошибка запроса подкатегорий");
        };
        xhr.send();
    }

    // Обновление при смене категории
    categorySelect.addEventListener("change", function () {
        // Сбрасываем выбранную подкатегорию
        subCategorySelect.value = "";
        updateSubCategories();
    });

    // Если категория уже выбрана при загрузке формы
    if (categorySelect.value) {
        updateSubCategories();
    }
});
