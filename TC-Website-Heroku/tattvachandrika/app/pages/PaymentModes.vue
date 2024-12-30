<template>
  <div class="container mx-auto mt-8 px-6">
    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-6">
      <ol class="flex space-x-2 text-sm text-gray-600">
        <li>
          <router-link
            to="/HomePage"
            class="text-blue-600 hover:text-blue-800 hover:underline"
            >Home</router-link
          >
        </li>
        <li><span>/</span></li>
        <li class="text-gray-500" aria-current="page">Payment Modes</li>
      </ol>
    </nav>

    <!-- Header Section -->
    <h2 class="text-3xl font-semibold text-gray-800 mb-6">Payment Modes</h2>

    <!-- Add Payment Mode Button -->
    <button
      class="bg-gradient-to-r from-blue-500 to-purple-600 text-white px-6 py-2 rounded-full shadow-lg hover:from-purple-600 hover:to-blue-500 transition duration-200 focus:outline-none focus:ring-4 focus:ring-blue-400 mb-6"
      @click="addMode"
    >
      Add Payment Mode
    </button>

    <!-- Payment Modes Table -->
    <div class="overflow-hidden rounded-lg shadow-lg bg-white">
      <table class="min-w-full bg-white divide-y divide-gray-200">
        <thead class="bg-gradient-to-r from-gray-100 to-gray-200">
          <tr>
            <th
              class="px-6 py-4 text-left text-xs font-medium text-gray-600 uppercase tracking-wider"
            >
              Name
            </th>
            <th
              class="px-6 py-4 text-left text-xs font-medium text-gray-600 uppercase tracking-wider"
            >
              Actions
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="mode in paymentModes"
            :key="mode._id || mode.tempId"
            class="hover:bg-gray-100 transition duration-200"
          >
            <td class="px-6 py-4">
              <input
                v-if="editModeId === (mode._id || mode.tempId)"
                type="text"
                v-model="mode.name"
                class="border border-gray-300 px-4 py-2 rounded-md focus:ring-2 focus:ring-blue-300 w-full"
              />
              <span
                v-else
                class="px-6 py-4 text-md font-semibold text-gray-700 font-sans"
                >{{ mode.name }}</span
              >
            </td>
            <td class="px-6 py-4 space-x-3">
              <!-- Save and Cancel buttons when editing -->
              <button
                v-if="editModeId === (mode._id || mode.tempId)"
                class="bg-green-500 text-white px-4 py-2 rounded-md text-xs shadow-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-400"
                @click="saveMode(mode)"
              >
                Save
              </button>
              <button
                v-if="editModeId === (mode._id || mode.tempId)"
                class="bg-gray-500 text-white px-4 py-2 rounded-md text-xs shadow-md hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-400"
                @click="cancelEdit(mode)"
              >
                Cancel
              </button>

              <!-- Edit button if not editing -->
              <button
                v-else
                class="bg-yellow-500 text-white px-4 py-2 rounded-md text-xs shadow-md hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-400"
                @click="editMode(mode._id || mode.tempId)"
              >
                Edit
              </button>

              <!-- Delete button, only show if the mode has an _id (i.e., it has been saved) -->
              <button
                v-if="mode._id && editModeId !== (mode._id || mode.tempId)"
                class="bg-red-500 text-white px-4 py-2 rounded-md text-xs shadow-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-400"
                @click="confirmDeleteMode(mode._id)"
              >
                Delete
              </button>
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
import paymentModeService from "../services/paymentModeService";
import confirmationModal from "./ConfirmationModal.vue";

export default {
  components: {
    confirmationModal,
  },
  data() {
    return {
      paymentModes: [], // Store the list of payment modes
      originalMode: null, // Store the original state of the mode being edited
      editModeId: null, // Track which mode is being edited
      showConfirmationModal: false, // Flag for showing the delete confirmation modal
      modeToDelete: null, // Track which mode is selected for deletion
    };
  },
  created() {
    this.loadPaymentModes(); // Load payment modes when the component is created
  },
  methods: {
    // Load all payment modes from the server
    loadPaymentModes() {
      paymentModeService
        .getPaymentModes()
        .then((response) => {
          this.paymentModes = response.data;
        })
        .catch((error) => {
          console.error(
            "There was an error retrieving the payment modes!",
            error
          );
        });
    },
    // Add a new payment mode with a temporary ID
    addMode() {
      const newMode = {
        tempId: Date.now(), // Temporary ID for the unsaved new mode
        name: "",
      };
      this.paymentModes.unshift(newMode); // Add to the beginning of the array
      this.editModeId = newMode.tempId; // Set the new mode in edit mode
    },
    // Edit an existing mode, saving its original state
    editMode(modeId) {
      const mode = this.paymentModes.find(
        (m) => (m._id || m.tempId) === modeId
      );
      if (mode) {
        this.originalMode = { ...mode }; // Save the original state before editing
      }
      this.editModeId = modeId; // Set the selected mode in edit mode
    },
    // Save the changes made to the mode
    saveMode(mode) {
      if (mode._id) {
        // Update an existing mode
        paymentModeService
          .updatePaymentMode(mode._id, mode)
          .then(() => {
            this.loadPaymentModes(); // Reload payment modes
            this.editModeId = null; // Exit edit mode
          })
          .catch((error) => {
            console.error(
              "There was an error updating the payment mode!",
              error
            );
          });
      } else {
        // Create a new mode
        paymentModeService
          .createPaymentMode(mode)
          .then(() => {
            this.loadPaymentModes(); // Reload payment modes
            this.editModeId = null; // Exit edit mode
          })
          .catch((error) => {
            console.error(
              "There was an error creating the payment mode!",
              error
            );
          });
      }
    },
    // Cancel editing and restore the original mode
    cancelEdit(mode) {
  if (mode._id) {
    // If it's an existing mode, restore its original value
    const index = this.paymentModes.findIndex(m => m._id === mode._id);
    if (index !== -1) {
      // Directly modify the object in Vue 3
      this.paymentModes[index] = { ...this.originalMode };
    }
  } else {
    // If it's a new unsaved mode, remove it from the list
    this.paymentModes = this.paymentModes.filter(m => m.tempId !== mode.tempId);
  }
  this.editModeId = null; // Exit edit mode
},
    // Show the delete confirmation modal
    confirmDeleteMode(modeId) {
      this.modeToDelete = modeId; // Set the mode to be deleted
      this.showConfirmationModal = true; // Show the confirmation modal
    },
    // Hide the delete confirmation modal
    hideDeleteModal() {
      this.showConfirmationModal = false;
    },
    // Delete the selected mode
    deleteMode() {
      if (this.modeToDelete) {
        paymentModeService
          .deletePaymentMode(this.modeToDelete)
          .then(() => {
            this.loadPaymentModes(); // Reload payment modes
            this.hideDeleteModal(); // Hide the delete modal
          })
          .catch((error) => {
            console.error(
              "There was an error deleting the payment mode!",
              error
            );
          });
      }
    },
  },
};
</script>

<style scoped>
/* Add custom styles here */
</style>
