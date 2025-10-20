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


// Функция изменения количества голосов
async function sendIncreaseScore() {
    const scoreButtons = Array.from(document.querySelectorAll('.main__button_increase_score'));
    [].forEach.call(scoreButtons, function(element) {
        element.onclick = function () {
            const score_increment = element.innerText;
            const element_with_id = element.closest('.main__card');
            const id = element_with_id.id
            fetch('/change_score', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({id: id, score_increment: score_increment})
            });
        };
    });
};


// Функция отправки комментария
async function sendComment() {
    const commentsInput = Array.from(document.querySelectorAll('.main__сard_comment'));
    [].forEach.call(commentsInput, function(element) {
        const comment = element.value.trim();
        const element_with_id = element.closest('.main__card');
        const id = element_with_id.id
        if (!comment) return;
        fetch('/send_comment', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({id: id, comment: comment})
        });
        element.value = '';
    });
};