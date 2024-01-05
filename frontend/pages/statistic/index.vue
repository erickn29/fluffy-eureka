<template>
  <section>
    <h1 id="h1tag">Statistic</h1>
    <div class="btn btn-primary" @click="sendData">Push</div>
    {{ responseData }}
  </section>
</template>

<script setup>
import $ from 'jquery'

const responseData = ref("");

const sendData = async () => {
  $('#h1tag').text('ttt')
  try {
    // Отправьте данные на сервер, используя, например, fetch или axios
    const response = await $fetch("/api/apiv1?name=Joe", {
      method: "POST",
      body: { age: 33 },
    });

    const data = response;
    responseData.value = data.message; // Обновите данные после успешной отправки
  } catch (error) {
    console.error("Ошибка при отправке данных:", error);
  }
};
</script>