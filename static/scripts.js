// Функционал добавления модульного окна
let decreaseScoreButtons = Array.from(document.querySelectorAll('.main__button_decrease_score'));
let modal = document.querySelector('.main__modal_decrease_score');
// Перебираем все найденные кнопки уменьшения количества голосов и добавляем на них события
[].forEach.call(decreaseScoreButtons, function(element) {
    // Добавляем событие по нажатию
    element.onclick = function() {
        // Действие
        modal.classList.add('modal_show')
    }
});


modal.onclick = function() {
    modal.classList.remove('modal_show');
};


// Функционал изменения количества голосов
const score_buttons = Array.from(document.querySelectorAll('.main__button_increase_score'));
[].forEach.call(score_buttons, function(element) {
    element.onclick = function() {
        // Находим инкремент рейтинга
        const score_increment = element.innerText;
        // Находим id карточки
        const element_with_id = element.closest('.main__card');
        const id = element_with_id.id
        // Находим значение рейтинга, увеличиваем и заменяем на текущей странице
        const score_element = element_with_id.querySelector('.main__score_value')
        score_value = score_element.textContent
        score_value++
        score_element.textContent = score_value
        // Отправляем увеличение рейтинга в базу данных на сервер
        fetch('/change_score', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({id: id, score_increment: score_increment})
        });
    };
});


// Функционал отправки комментария
const commentsInput = Array.from(document.querySelectorAll('.main__сard_send_comment'));
[].forEach.call(commentsInput, function(element) {
    element.onclick = function() {
        // Находим id карточки
        const element_with_id = element.closest('.main__card');
        const id = element_with_id.id
        // Находим текст комментария
        comment_element = element_with_id.querySelector('.main__сard_comment_input')
        const comment = comment_element.value.trim();
        if (!comment) return;
        // Добавляем комментарий на страницу
        const comments_element = element_with_id.querySelector('.main__сard_comments')
        comments_element.innerHTML += `${comment}<br>`;
        comments_element.scrollTop = comments_element.scrollHeight;
        // Отправляем комментарий в базу данных на сервер
        fetch('/send_comment', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({id: id, comment: comment})
        });
        comment_element.value = '';
    };
});
