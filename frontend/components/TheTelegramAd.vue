<template>
  <div @click="getTelegramChannel" class="ad telegram sticky-top">
    <div class="ad-text mb-2 d-flex align-content-center">
      Полезные статьи, дайджест вакансий каждый день!
    </div>
    <hr>  
    <div class="row  px-2 py-2">
      <div class="col-3">
        <!-- <img src="assets/img/tg.svg.webp" width="40px"> -->
        <img src="assets/img/me.jpg" width="44px" style="border-radius: 50%;">
      </div>
      <div class="col-8">
        <strong>Подпишись на мой телеграм-канал!</strong>
      </div>
    </div>
  </div>
</template>

<script setup>
const getTelegramChannel = () => {
  window.open("https://t.me/geekhunter_ru", "_blank");
}
</script>
