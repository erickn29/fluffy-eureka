<template>
  <section>
    <div class="post" v-if="posts.results.length > 0">
      <div class="post-item row d-flex justify-content-center mb-5" v-for="post in posts.results" :key="post.id">
        
        <div class="post-link my-2 col-lg-6 mb-4" v-if="post.poster_link">
          <img :src="post.poster_link">
        </div>
        <!-- <div class="post-link mb-2" v-else>
          Место для картинки
        </div> -->
        <div class="post-text col-lg-6">
          <NuxtLink :to="'/post/' + post.id"><h2>{{ post.title }}</h2></NuxtLink>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quam ducimus sint fuga expedita unde non impedit, quidem similique, voluptates assumenda quas culpa magnam quasi ut quos eos incidunt quod eaque.
        </div>
      </div>
    </div>
    <div v-else>
        No content
    </div>
  </section>
</template>

<script setup>

const { data: posts } = await useFetch("http://127.0.0.1:8000/post/");

const colors = [
  'red',
  'green',
  'blue',
  'orange',
  'purple',
  'aqua'
]

const colorIt = () => {
  $('.post-link').each(function () {
    console.log($(this))
    $(this).addClass(colors[Math.floor(Math.random() * colors.length)])
  })
}

onMounted(() => {
  // colorIt()
});

</script>

<style>

img {
  max-height: 300px;
  max-width: 430px;
}

h2{
  font-size: 1.3rem;
  color: #42b8a5;
  font-weight: 700;
}
.post-link {
  display: flex;
  max-height: 300px;
  flex-wrap: nowrap;
  justify-content: start;
  padding: 0;
}
.red { background: linear-gradient(45deg, red, white); }
.green { background: linear-gradient(45deg, green, white); }
.blue { background: linear-gradient(45deg, blue, white); }
.orange { background: linear-gradient(45deg, orange, white); }
.purple { background: linear-gradient(45deg, purple, white); }
.aqua { background: linear-gradient(45deg, aqua, white); }

</style>
