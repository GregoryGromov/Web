<template>
  <main class=" container text-white">
    <div v-for="post in posts" :key="post.id" class="my-4 mx-6">
      <div class="bg-teal-900 px-8 py-6"> 
        <h1>{{ post.title }}</h1>
      </div>
      
    </div>
</main>
</template>


<script setup>
import { ref, onMounted } from "vue";
import axios from 'axios';

const posts = ref({});

onMounted(() => {
  axios.get('https://jsonplaceholder.typicode.com/posts')
    .then(response => posts.value = response.data)
})

</script>