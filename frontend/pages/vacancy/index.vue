<template>
  <section>
    <h1 class="mb-4">Найдено вакансий: {{ countItems }}</h1>
    <hr />
    <div class="search-form row">
      <div class="search-speciality col-lg-3 mb-4">
        <label class="mb-2" for="speciality">Специализация</label>
        <select id="speciality" class="form-control">
          <option v-for="item in specialities" :key="item" :value="item.name">
            {{ item.name }}
          </option>
        </select>
      </div>
      <div class="search-grade col-lg-3 mb-4">
        <label class="mb-2" for="grade">Уровень</label>
        <select id="grade" class="form-control">
          <option v-for="item in grades" :key="item" :value="item.name">
            {{ item.name }}
          </option>
        </select>
      </div>
      <div class="search-location col-lg-3 mb-4">
        <label class="mb-2" for="location">Город</label>
        <select id="location" class="form-control">
          <option value="remote">Удаленно</option>
          <option v-for="item in cities" :key="item" :value="item.name">
            {{ item.name }}
          </option>
        </select>
      </div>
      <div class="search-salary col-lg-3 mb-4">
        <label class="mb-2" for="salary">Зарплата от</label>
        <input id="salary" class="form-control" type="number" value="30000" />
      </div>
    </div>
    <div class="d-flex justify-content-start mb-4 col-12">
      <button
        @click="fetchData('http://127.0.0.1:8000/api/v1/vacancy/', true)"
        class="btn btn-success"
      >
        Искать
      </button>
    </div>
    <div v-if="vacancies.length > 0">
      <div v-for="vacancy in vacancies" :key="vacancy.id">
        <VacancyListItem :vacancy="vacancy" />
      </div>
    </div>
    <div style="min-height: 555px;" class="d-flex justify-content-center" v-else><TheLoader/></div>
    <div v-if="nextPageUrl" class="d-flex justify-content-center mb-4">
      <button @click="next" class="btn btn-success" style="width: 100%">
        Показать ещё
      </button>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import TheLoader from "~/components/TheLoader.vue";

// Используем реактивное значение для хранения данных
const vacancies = ref([]);
// Используем реактивное значение для хранения ссылки на следующую страницу
const nextPageUrl = ref(null);
const countItems = ref(0);
const specialities = ref([]);
const grades = ref([]);
const cities = ref([]);

// Функция для загрузки данных
const fetchData = async (url, getSearch) => {
  if (getSearch) {
    url = url + '?' +
    'salary_from=' + $('#salary').val() + '&' +
    'location=' + $('#location').val() + '&' +
    // 'is_remote=' + $('#is_remote').val() + '&' +
    'speciality=' + $('#speciality').val() + '&' +
    'grade=' + $('#grade').val()

    vacancies.value = []
  }
  const response = await $fetch(url);
  // console.log(response)
  const { results, next, count } = await response;
  // vacancies.value = []; // Очищаем текущий массив vacancies
  // Добавляем новые данные
  // results.forEach((item) => {
  //   vacancies.value.push(item);
  // });

  // console.log(results)
  // Обновляем значения
  vacancies.value = [...vacancies.value, ...results];
  // vacancies.value = results
  nextPageUrl.value = next;
  countItems.value = count;
};

const fetchSpeciality = async (url) => {
  const response = await $fetch(url);
  const { results } = await response;
  specialities.value = results;
};

const fetchGrade = async (url) => {
  const response = await $fetch(url);
  const { results } = await response;
  grades.value = results;
};

const fetchCity = async (url) => {
  const response = await $fetch(url);
  const { results } = await response;
  cities.value = results;
};

// Функция для загрузки следующей страницы
const next = () => {
  if (nextPageUrl.value) {
    fetchData(nextPageUrl.value);
  }
};

// Загрузка данных при монтировании компонента
onMounted(() => {
  fetchData("http://127.0.0.1:8000/api/v1/vacancy/", false);
  fetchSpeciality("http://127.0.0.1:8000/api/v1/speciality/");
  fetchGrade("http://127.0.0.1:8000/api/v1/grade/");
  fetchCity("http://127.0.0.1:8000/api/v1/city/");
});
</script>

<style>
.form-control {
  background: #020420 !important;
  color: #e3e3e3;
  border: 1px solid #e3e3e354;
  border-radius: 10px;
}
.form-control:focus {
  color: #e3e3e3;
  background-color: #020420 !important;
  border-color: #70308c;
  outline: 0;
  box-shadow: none !important;
}
</style>