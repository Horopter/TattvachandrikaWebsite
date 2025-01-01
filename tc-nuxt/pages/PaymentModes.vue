<template>
  <div class="container mx-auto mt-8 px-6">
    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-6">
      <ol class="flex space-x-2 text-sm text-gray-600">
        <li>
          <router-link to="/HomePage" class="text-blue-600 hover:text-blue-800 hover:underline">Home</router-link>
        </li>
        <li><span>/</span></li>
        <li class="text-gray-500" aria-current="page">Payment Modes</li>
      </ol>
    </nav>

    <!-- Header Section -->
    <h2 class="text-3xl font-semibold text-gray-800 mb-6">Payment Modes</h2>

    <!-- Add Payment Mode Button -->
    <button class="bg-gradient-to-r from-blue-500 to-purple-600 text-white px-6 py-2 rounded-full shadow-lg hover:from-purple-600 hover:to-blue-500 transition duration-200 focus:outline-none focus:ring-4 focus:ring-blue-400 mb-6" @click="addMode">
      Add Payment Mode
    </button>

    <!-- Payment Modes Table -->
    <div class="overflow-hidden rounded-lg shadow-lg bg-white">
      <table class="min-w-full bg-white divide-y divide-gray-200">
        <thead class="bg-gradient-to-r from-gray-100 to-gray-200">
          <tr>
            <th class="px-6 py-4 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Name</th>
            <th class="px-6 py-4 text-left text-xs font-medium text-gray-600 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="mode in paymentModes" :key="mode._id" class="hover:bg-gray-100 transition duration-200">
            <td class="px-6 py-4">
              <input v-if="editModeId === mode._id" type="text" v-model="mode.name" class="border border-gray-300 px-4 py-2 rounded-md focus:ring-2 focus:ring-blue-300 w-full"/>
              <span v-else class="px-6 py-4 text-md font-semibold text-gray-700 font-sans">{{ mode.name }}</span>
            </td>
            <td class="px-6 py-4 space-x-3">
              <button v-if="editModeId === mode._id" class="bg-green-500 text-white px-4 py-2 rounded-md text-xs shadow-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-400" @click="saveMode(mode)">Save</button>
              <button v-else class="bg-yellow-500 text-white px-4 py-2 rounded-md text-xs shadow-md hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-400" @click="editMode(mode._id)">Edit</button>
              <button class="bg-red-500 text-white px-4 py-2 rounded-md text-xs shadow-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-400" @click="confirmDeleteMode(mode._id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Confirmation Modal -->
    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this payment mode?"
      @close="hideDeleteModal"
      @confirm="deleteMode"
    />
  </div>
</template>

<script>
import paymentModeService from '../services/paymentModeService';
import confirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    confirmationModal
  },
  data() {
    return {
      paymentModes: [],
      editModeId: null,
      showConfirmationModal: false,
      modeToDelete: null
    };
  },
  created() {
    this.loadPaymentModes();
  },
  methods: {
    loadPaymentModes() {
      paymentModeService.getPaymentModes().then(response => {
        this.paymentModes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the payment modes!", error);
      });
    },
    addMode() {
      const newMode = {
        name: ''
      };
      this.paymentModes.unshift(newMode);
      this.editModeId = newMode._id;
    },
    editMode(modeId) {
      this.editModeId = modeId;
    },
    saveMode(mode) {
      if (mode._id) {
        paymentModeService.updatePaymentMode(mode._id, mode).then(() => {
          this.loadPaymentModes();
          this.editModeId = null;
        }).catch(error => {
          console.error("There was an error updating the payment mode!", error);
        });
      } else {
        paymentModeService.createPaymentMode(mode).then(() => {
          this.loadPaymentModes();
          this.editModeId = null;
        }).catch(error => {
          console.error("There was an error creating the payment mode!", error);
        });
      }
    },
    confirmDeleteMode(modeId) {
      this.modeToDelete = modeId;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
    },
    deleteMode() {
      if (this.modeToDelete) {
        paymentModeService.deletePaymentMode(this.modeToDelete).then(() => {
          this.loadPaymentModes();
          this.hideDeleteModal();
        }).catch(error => {
          console.error("There was an error deleting the payment mode!", error);
        });
      }
    }
  }
};
</script>

<style scoped>
/* Add custom styles here */
</style>
