<template>
  <div>
    ERROR
    {{ error.statusCode }}
    {{ error.message }}
  </div>
</template>

<script setup>
  defineProps(["error"]);
</script>