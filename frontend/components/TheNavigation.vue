<template>
  <div class="container sticky-top">
    <nav class="navbar">
      <a href="/" class="navbar-brand">PYTHON RUSSIA</a>
      <div class="nav-links d-flex gap-3">
        <NuxtLink to="/post">Статьи</NuxtLink>
        <NuxtLink to="/vacancy">Вакансии</NuxtLink>
        <NuxtLink to="/statistic">Статистика</NuxtLink>
      </div>
    </nav>
  </div>
</template>

<style>
.navbar {
  background: #02042075;
  backdrop-filter: blur(8px);
}

.navbar a{
  font-weight: 600;
}

.navbar-brand {
  font-weight: 900 !important;
  /* color: #42b883; */
  background: -webkit-linear-gradient(45deg, #42b883, #42b8b8);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.navbar-brand:hover {
  color: #42b883;
  text-shadow: 0 0 10px #42b88333;
}
</style>