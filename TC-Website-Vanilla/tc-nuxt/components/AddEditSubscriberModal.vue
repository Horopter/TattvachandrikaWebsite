<template>
  <div v-if="show" class="fixed inset-0 z-50 flex items-center justify-center bg-gray-900 bg-opacity-50" tabindex="-1" role="dialog">
    <div class="bg-white rounded-lg shadow-lg w-full max-w-lg">
      <div class="flex justify-between items-center p-4 border-b">
        <h5 class="text-lg font-semibold">{{ modalTitle }}</h5>
        <button type="button" class="text-gray-600 hover:text-gray-900" @click="close" aria-label="Close">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
      <div class="p-4">
        <form @submit.prevent="handleSubmit">
          <div class="mb-4">
            <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
            <input type="text" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="name" v-model="localSubscriber.name" required>
          </div>
          <div class="mb-4">
            <label for="registration_number" class="block text-sm font-medium text-gray-700">Registration Number</label>
            <input type="text" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="registration_number" v-model="localSubscriber.registration_number" required>
          </div>
          <div class="mb-4">
            <label for="address" class="block text-sm font-medium text-gray-700">Address</label>
            <input type="text" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="address" v-model="localSubscriber.address">
          </div>
          <div class="mb-4">
            <label for="city_town" class="block text-sm font-medium text-gray-700">City/Town</label>
            <input type="text" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="city_town" v-model="localSubscriber.city_town">
          </div>
          <div class="mb-4">
            <label for="state" class="block text-sm font-medium text-gray-700">State</label>
            <input type="text" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="state" v-model="localSubscriber.state">
          </div>
          <div class="mb-4">
            <label for="pincode" class="block text-sm font-medium text-gray-700">Pincode</label>
            <input type="text" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="pincode" v-model="localSubscriber.pincode">
          </div>
          <div class="mb-4">
            <label for="phone" class="block text-sm font-medium text-gray-700">Phone</label>
            <input type="text" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="phone" v-model="localSubscriber.phone">
          </div>
          <div class="mb-4">
            <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
            <input type="email" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="email" v-model="localSubscriber.email" required>
          </div>
          <div class="mb-4">
            <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
            <select class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="category" v-model="localSubscriber.category">
              <option v-for="category in categories" :value="category._id" :key="category._id">{{ category.name }}</option>
            </select>
          </div>
          <div class="mb-4">
            <label for="stype" class="block text-sm font-medium text-gray-700">Type</label>
            <select class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="stype" v-model="localSubscriber.stype">
              <option v-for="type in types" :value="type._id" :key="type._id">{{ type.name }}</option>
            </select>
          </div>
          <div class="mb-4">
            <label for="notes" class="block text-sm font-medium text-gray-700">Notes</label>
            <textarea class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" id="notes" v-model="localSubscriber.notes"></textarea>
          </div>
          <div class="flex justify-end space-x-2">
            <button type="submit" class="px-4 py-2 bg-indigo-600 text-white font-semibold rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">{{ modalButton }}</button>
            <button type="button" class="px-4 py-2 bg-gray-300 text-gray-700 font-semibold rounded-md shadow-sm hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500" @click="close">Cancel</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    subscriber: Object,
    categories: Array,
    types: Array
  },
  data() {
    return {
      localSubscriber: { ...this.subscriber }
    };
  },
  computed: {
    modalTitle() {
      return this.localSubscriber && this.localSubscriber._id ? 'Edit Subscriber' : 'Add Subscriber';
    },
    modalButton() {
      return this.localSubscriber && this.localSubscriber._id ? 'Update' : 'Add';
    }
  },
  watch: {
    subscriber(newVal) {
      this.localSubscriber = { ...newVal };
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    handleSubmit() {
      this.$emit('save', this.localSubscriber);
      this.close();
    }
  }
};
</script>

<style scoped>
/* No additional styles needed for Tailwind CSS */
</style>
