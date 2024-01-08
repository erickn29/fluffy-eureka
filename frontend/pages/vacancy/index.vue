<template>
  <section>
    <h1 class="mb-4">Новых вакансий за последние 30 дней: {{ countItems }}</h1>
    <hr>
    <div v-if="vacancies.length > 0">
      <div v-for="vacancy in vacancies" :key="vacancy.id">
        <VacancyListItem :vacancy="vacancy" />
      </div>
    </div>
    <div v-else>
      Загружаю данные...
    </div>
    <div v-if="nextPageUrl" class="d-flex justify-content-center mb-4">
      <button @click="next" class="btn btn-success" style="width: 100%;">Показать ещё</button>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// Используем реактивное значение для хранения данных
const vacancies = ref([]);

// Используем реактивное значение для хранения ссылки на следующую страницу
const nextPageUrl = ref(null);

const countItems = ref(0)

// Функция для загрузки данных
const fetchData = async (url) => {
  const response = await $fetch(url);
  // console.log(response)
  const { results, next, count } = await response;
  // vacancies.value = []; // Очищаем текущий массив vacancies
  // Добавляем новые данные
  // results.forEach((item) => {
  //   vacancies.value.push(item);
  // });

  console.log(results)  
  // Обновляем значения
  vacancies.value = [...vacancies.value, ...results];
  // vacancies.value = results
  nextPageUrl.value = next;
  countItems.value = count
};

// Функция для загрузки следующей страницы
const next = () => {
  if (nextPageUrl.value) {
    fetchData(nextPageUrl.value);
  }
};

// Загрузка данных при монтировании компонента
onMounted(() => {
  fetchData("http://127.0.0.1:8000/api/v1/vacancy/");
});
</script>