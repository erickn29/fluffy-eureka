<template>
  <div>
    <TheNavigation />
    <div class="container my-4">
      <div class="row">
        <div class="col-md-9">
          <slot />
        </div>
        <div class="col-md-3">right menu</div>
      </div>
    </div>
    <TheFooter />
  </div>
</template>

<style>
</style>
