<template>
  <div class="container sticky-top" style="backdrop-filter: blur(8px); background: #02042075;">
    <nav class="navbar">
      <a href="/" class="navbar-brand"><i class="fa-brands fa-python" style="font-size: 1.25rem;"></i> PYTHON RUSSIA</a>
      <div class="nav-links d-flex gap-3">
        <NuxtLink to="/post">Статьи</NuxtLink>
        <NuxtLink to="/vacancy">Вакансии</NuxtLink>
        <NuxtLink to="/statistic">Статистика</NuxtLink>
      </div>
    </nav>
  </div>
</template>

<style>
/* .navbar { */
  /* background: #02042075; */
  /* backdrop-filter: blur(8px); */
/* } */

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