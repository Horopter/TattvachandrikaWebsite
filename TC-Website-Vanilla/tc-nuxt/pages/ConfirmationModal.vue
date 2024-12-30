<template>
  <div v-if="show" class="fixed inset-0 z-50 flex items-center justify-center bg-gray-900 bg-opacity-50" tabindex="-1" role="dialog">
    <div class="bg-white rounded-lg shadow-lg w-full max-w-sm">
      <div class="flex justify-between items-center p-4 border-b">
        <h5 class="text-lg font-semibold">{{ title }}</h5>
        <button type="button" class="text-gray-600 hover:text-gray-900" @click="close" aria-label="Close">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
      <div class="p-4">
        <p>{{ message }}</p>
      </div>
      <div class="flex justify-end space-x-2 p-4 border-t">
        <button type="button" class="px-4 py-2 bg-gray-300 text-gray-700 font-semibold rounded-md shadow-sm hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500" @click="close">Cancel</button>
        <button type="button" class="px-4 py-2 bg-red-600 text-white font-semibold rounded-md shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500" @click="confirm">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    title: String,
    message: String
  },
  methods: {
    close() {
      this.$emit('close');
    },
    confirm() {
      this.$emit('confirm');
    }
  }
};
</script>

<style scoped>
/* No additional styles needed for Tailwind CSS */
</style>
