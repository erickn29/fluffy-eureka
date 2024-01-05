<template>
  <section>
    <h1>Vacancy list</h1>
    <div v-if="vacancies.results.length > 0">
      <div v-for="vacancy in vacancies.results" :key="vacancy.id">
        <VacancyListItem :vacancy="vacancy" />
      </div>
    </div>
    <div v-else>
      No content
    </div>
  </section>
</template>

<script setup>
const { data: vacancies } = await useFetch(
  "http://127.0.0.1:8000/api/v1/vacancy/"
);
</script>