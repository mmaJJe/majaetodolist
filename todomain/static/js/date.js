const date = document.querySelector(".date")
const days = document.querySelector(".days")


const today = new Date()

const dateString = today.toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
});
const dayName = today.toLocaleDateString('ko-KR', { weekday: 'long' });

date.innerHTML = dateString;
days.innerHTML = dayName;