<template>
  <div v-if="show" class="fixed bottom-4 right-4 p-4 z-50">
    <div :class="`bg-${variant}-600 text-white rounded-lg shadow-lg p-4 flex flex-col`">
      <div class="flex items-center justify-between">
        <strong class="text-lg font-semibold">{{ title }}</strong>
        <button type="button" class="text-white hover:text-gray-200" @click="hideToast" aria-label="Close">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
      <div class="mt-2">
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      message: '',
      title: '',
      variant: 'green', // Default to 'green' for success
    };
  },
  methods: {
    showToast(message, title = 'Notification', variant = 'green') {
      this.message = message;
      this.title = title;
      this.variant = variant;
      this.show = true;

      setTimeout(() => {
        this.show = false;
      }, 15000); // Show for 15 seconds
    },
    hideToast() {
      this.show = false;
    }
  }
};
</script>

<style scoped>
/* Add any additional styles if necessary */
</style>
