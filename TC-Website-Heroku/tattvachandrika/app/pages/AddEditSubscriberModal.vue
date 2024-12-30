<template>
  <div
    v-if="show"
    class="fixed inset-0 z-50 flex items-center justify-center bg-gray-900 bg-opacity-50 overflow-y-auto"
    tabindex="-1"
    role="dialog"
  >
    <div class="bg-white rounded-lg shadow-lg w-full max-w-lg flex flex-col max-h-[80vh]">
      <!-- Header -->
      <div class="flex justify-between items-center p-4 border-b flex-shrink-0">
        <h5 class="text-xl font-semibold">{{ modalTitle }}</h5>
        <button
          type="button"
          class="text-gray-600 hover:text-gray-900"
          @click="close"
          aria-label="Close"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            ></path>
          </svg>
        </button>
      </div>

      <!-- Content -->
      <div class="p-6 flex-1 overflow-y-auto">
        <form @submit.prevent="handleSubmit">
          <!-- Name -->
          <div class="mb-4">
            <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
            <input
              type="text"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="name"
              v-model="localSubscriber.name"
              required
            />
          </div>
          <!-- Registration Number -->
          <div class="mb-4">
            <label for="registration_number" class="block text-sm font-medium text-gray-700">Registration Number</label>
            <input
              type="text"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="registration_number"
              v-model="localSubscriber.registration_number"
              required
            />
          </div>
          <!-- Address -->
          <div class="mb-4">
            <label for="address" class="block text-sm font-medium text-gray-700">Address</label>
            <input
              type="text"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="address"
              v-model="localSubscriber.address"
            />
          </div>
          <!-- City/Town -->
          <div class="mb-4">
            <label for="city_town" class="block text-sm font-medium text-gray-700">City/Town</label>
            <input
              type="text"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="city_town"
              v-model="localSubscriber.city_town"
            />
          </div>
          <!-- State -->
          <div class="mb-4">
            <label for="state" class="block text-sm font-medium text-gray-700">State</label>
            <input
              type="text"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="state"
              v-model="localSubscriber.state"
            />
          </div>
          <!-- Pincode -->
          <div class="mb-4">
            <label for="pincode" class="block text-sm font-medium text-gray-700">Pincode</label>
            <input
              type="text"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="pincode"
              v-model="localSubscriber.pincode"
            />
          </div>
          <!-- Phone -->
          <div class="mb-4">
            <label for="phone" class="block text-sm font-medium text-gray-700">Phone</label>
            <input
              type="text"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="phone"
              v-model="localSubscriber.phone"
            />
          </div>
          <!-- Email -->
          <div class="mb-4">
            <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
            <input
              type="email"
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="email"
              v-model="localSubscriber.email"
              required
            />
          </div>
          <!-- Category -->
          <div class="mb-4">
            <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
            <select
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="category"
              v-model="localSubscriber.category"
            >
              <option v-for="category in categories" :value="category._id" :key="category._id">
                {{ category.name }}
              </option>
            </select>
          </div>
          <!-- Type -->
          <div class="mb-4">
            <label for="stype" class="block text-sm font-medium text-gray-700">Type</label>
            <select
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="stype"
              v-model="localSubscriber.stype"
            >
              <option v-for="t in types" :value="t._id" :key="t._id">
                {{ t.name }}
              </option>
            </select>
          </div>
          <!-- Notes -->
          <div class="mb-4">
            <label for="notes" class="block text-sm font-medium text-gray-700">Notes</label>
            <textarea
              class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-base p-2"
              id="notes"
              v-model="localSubscriber.notes"
            ></textarea>
          </div>
          <!-- Note: Removed action buttons from here -->
        </form>
      </div>

      <!-- Footer -->
      <div class="flex justify-end space-x-2 p-4 border-t flex-shrink-0">
        <button
          type="submit"
          class="px-6 py-2 bg-indigo-600 text-white font-semibold rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          @click="handleSubmit"
        >
          {{ modalButton }}
        </button>
        <button
          type="button"
          class="px-6 py-2 bg-gray-300 text-gray-700 font-semibold rounded-md shadow-sm hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
          @click="close"
        >
          Cancel
        </button>
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
/* Ensure the modal doesn't cause body scroll */
body {
  overflow: hidden;
}
</style>
