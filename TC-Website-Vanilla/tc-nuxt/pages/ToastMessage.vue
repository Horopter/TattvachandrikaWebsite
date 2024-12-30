<template>
    <div class="toast" v-if="visible">
      <span>{{ message }}</span>
      <button @click="close">✖</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      message: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        visible: true,
      };
    },
    methods: {
      close() {
        this.visible = false;
        this.$emit('close'); // Emit close event to parent
      },
    },
  };
  </script>
  
  <style scoped>
  .toast {
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 15px;
    background-color: #007bff;
    color: white;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  }
  
  .toast button {
    background: none;
    border: none;
    color: white;
    font-weight: bold;
    cursor: pointer;
  }
  </style>