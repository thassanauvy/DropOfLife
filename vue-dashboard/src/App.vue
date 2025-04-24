<template>
    <div class="min-h-screen bg-gray-100 text-gray-800 p-4">
      <h1 class="text-3xl font-bold mb-6">DropOfLife</h1>
      <Login />
    </div>
  </template>
  
  <script>
  import Login from './components/Login.vue'
  export default {
    components: { Login }
  }
  </script>
  