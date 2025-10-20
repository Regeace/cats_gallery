let decreaseScoreButtons = Array.from(document.querySelectorAll('.main__button_decrease_score'));
let modal = document.querySelector('.main__modal_decrease_score');

//Перебираем все найденные кнопки и добавляем на них события
[].forEach.call(decreaseScoreButtons, function(element) {
    //Добавляем событие по нажатию
    element.onclick = function(e) {
        //Действие
        modal.classList.add('modal_show')
    }
});

modal.onclick = function() {
    modal.classList.remove('modal_show');
};