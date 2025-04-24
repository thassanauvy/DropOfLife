<template>
    <div class="p-6">
      <h2 class="text-xl font-bold mb-4">Request Blood</h2>
      <form>
        <input class="w-full p-2 border mb-3" placeholder="Blood Type" />
        <textarea class="w-full p-2 border mb-3" placeholder="Reason"></textarea>
        <button class="bg-red-500 text-white p-2 rounded">Request</button>
      </form>
    </div>
  </template>
  <script>
  export default { name: 'RequestBlood' }
  </script>
  