<template>
  <Head>
    <Title>{{ post.title }}</Title>
    <Meta name="description" :content="post.text.slice(0, 50)" />
  </Head>
  <div>
    <div v-if="post">
      <h1>{{ post.title }}</h1>
      <hr>
      <div v-html="post.text"></div>
    </div>
    <div v-else>404</div>
  </div>
</template>

<script setup>
import hljs from "highlight.js";
const { id } = useRoute().params;

definePageMeta({
  layout: "default",
});

const { data: post } = await useFetch(
  "http://127.0.0.1:8000/post/" + id + "/"
);

setTimeout(function () {
  document.querySelectorAll("code").forEach((block) => {
    block.innerHTML = block.innerHTML.
      // replace(/&/g, "&amp;").
      replace('<code>', '').
      replace('<code class="language-plaintext">', '').
      replace('</code>', '').
      replace(/"/g, "&quot;").
      replace(/'/g, "&#039;")
      // replace(/&gt;/g, '>')
    hljs.highlightElement(block);
  });
}, 20);
</script>