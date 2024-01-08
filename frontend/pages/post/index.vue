<template>
  <section>
    <h1>Posts list</h1>
    <div v-if="posts.results.length > 0">
      <div v-for="post in posts.results" :key="post.id">
        <NuxtLink :to="'/post/' + post.id">{{ post.title }}</NuxtLink>
      </div>
    </div>
    <div v-else>
        No content
    </div>
  </section>
</template>

<script setup>
const { data: posts } = await useFetch("http://127.0.0.1:8000/post/");
</script>