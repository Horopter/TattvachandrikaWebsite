<template>
  <div class="toast-container position-fixed bottom-0 end-0 p-3" style="z-index: 1050;">
    <div v-if="show" class="toast show" role="alert" aria-live="assertive" aria-atomic="true">
      <div :class="`toast-header bg-${variant} text-white`">
        <strong class="me-auto">{{ title }}</strong>
        <button type="button" class="btn-close" @click="hideToast" aria-label="Close"></button>
      </div>
      <div class="toast-body">
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
      variant: 'success',
    };
  },
  methods: {
    showToast(message, title = 'Notification', variant = 'success') {
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
.toast-container {
  position: fixed;
  bottom: 0;
  right: 0;
  z-index: 1050;
}

.toast-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.toast-body {
  padding: 0.5rem;
}
</style>
