<template>
  <div class="container mx-auto mt-5 px-4">
    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-4">
      <ol class="flex space-x-2 text-gray-700">
        <li>
          <router-link to="/" class="text-blue-600 hover:text-blue-800">Home</router-link>
        </li>
        <li>
          <span>/</span>
        </li>
        <li class="text-gray-500" aria-current="page">Payment Modes</li>
      </ol>
    </nav>

    <h2 class="text-2xl font-bold mb-4">Payment Modes</h2>
    <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3" @click="addMode">Add Payment Mode</button>

    <table class="min-w-full bg-white divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="mode in paymentModes" :key="mode._id">
          <td class="px-6 py-4 text-sm text-gray-900">
            <input v-if="editModeId === mode._id" type="text" v-model="mode.name" class="border border-gray-300 px-2 py-1 rounded-md"/>
            <span v-else>{{ mode.name }}</span>
          </td>
          <td class="px-6 py-4 text-sm text-gray-900">
            <button class="bg-green-600 text-white px-3 py-1 rounded-md text-xs shadow-sm hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500" v-if="editModeId === mode._id" @click="saveMode(mode)">Save</button>
            <button class="bg-yellow-500 text-white px-3 py-1 rounded-md text-xs shadow-sm hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-400" v-else @click="editMode(mode._id)">Edit</button>
            <button class="bg-red-600 text-white px-3 py-1 rounded-md text-xs shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500" @click="confirmDeleteMode(mode._id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

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
/* You can add custom styles here if needed */
</style>
