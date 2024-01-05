<template>
  <div>
    <div v-if="vacancy.link">
      <a target="_blank" :href="vacancy.link">{{ vacancy.title }}</a>
    </div>
    <div v-else>
      <NuxtLink :to="'/vacancy/' + vacancy.id">{{ vacancy.title }}</NuxtLink>
    </div>
  </div>
</template>

<script setup>
const { vacancy } = defineProps(["vacancy"]);
</script>