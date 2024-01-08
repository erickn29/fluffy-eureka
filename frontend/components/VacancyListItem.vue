<template>
  <div class="mb-4">
    <div v-if="vacancy.link" class="vacancy-title">
      <a target="_blank" :href="vacancy.link">{{ vacancy.title }} { {{ vacancy.grade.name }} }</a>
    </div>
    <div v-else class="vacancy-title">
      <NuxtLink :to="'/vacancy/' + vacancy.id">{{ vacancy.title }} { {{}} }</NuxtLink>
    </div>

    <div class="vacancy-company">
      <i class="fa-solid fa-briefcase"></i> {{ vacancy.company.name }}
    </div>

    <div class="vacancy-location">
      <i class="fa-solid fa-location-dot"></i> {{ vacancy.company.city.name }}
    </div>

    <div v-if="vacancy.salary_from && vacancy.salary_to">
      <i class="fa-solid fa-coins"></i> от
      <span class="vacancy-salary"
        >{{ salary_mod(vacancy.salary_from) }} руб.</span
      >
      до <span class="vacancy-salary">{{ salary_mod(vacancy.salary_to) }} руб.</span>
    </div>
    <div v-else-if="vacancy.salary_from">
      <i class="fa-solid fa-coins"></i> от <span class="vacancy-salary">{{ salary_mod(vacancy.salary_from) }} руб.</span>
    </div>
    <div v-else>
      <i class="fa-solid fa-coins"></i> до <span class="vacancy-salary">{{ salary_mod(vacancy.salary_to) }} руб.</span>
    </div>

    <div class="vacancy-experience">
      Опыт: {{ vacancy.experience.name }}
    </div>

    <div v-if="vacancy.stack" class="vacancy-stack">
      <span class="stack-item" v-for="item in vacancy.stack" :key="item">
        {{ item }}
      </span>
    </div>

    <div class="vacanc-remote" v-if="vacancy.is_remote">
      <i class="fa-solid fa-house-user" style="color: #42b8a0"></i> Возможна удалённая работа
    </div>

    <div class="vacancy-date"><i class="fa-solid fa-calendar-days"></i> {{ vacancy.date }}</div>
  </div>
  <hr>
</template>

<script setup>
const { vacancy } = defineProps(["vacancy"]);
const salary_mod = function (salary) {
  return (
    salary.toString().slice(0, salary.toString().length - 3) +
    " " +
    salary.toString().slice(salary.toString().length - 3)
  );
};
</script>

<style>
i{
  font-size: .8rem;
}
.vacancy-title a {
  font-size: 1.1rem;
  font-weight: 700;
  color: #42b8a0;
}

.vacancy-salary {
  color: #e3e3e3;
  font-size: 1.1rem;
  font-weight: 600;
}

.stack-item{
  font-size: .75rem;
  padding: 2px 5px;
  background: #9d42b8b5;
  margin-right: 5px;
  border-radius: 3px;
  color: black;
  font-weight: 700;
}
</style>