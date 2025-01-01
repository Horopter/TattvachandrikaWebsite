<template>
  <div class="container mx-auto mt-8 px-6">
    <h2 class="text-3xl font-semibold text-gray-900 mb-6">Subscription Modes</h2>

    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-8">
      <ol class="flex space-x-2 text-gray-600">
        <li>
          <router-link to="/HomePage" class="text-indigo-600 hover:text-indigo-800 font-medium">Home</router-link>
        </li>
        <li>/</li>
        <li class="text-gray-500 font-medium" aria-current="page">Subscription Modes</li>
      </ol>
    </nav>

    <!-- Subscription Modes Table -->
    <div class="shadow-lg overflow-hidden border border-gray-300 sm:rounded-lg">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-100">
          <tr>
            <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 uppercase tracking-wider">Name</th>
            <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-100">
          <!-- Add New Mode Row -->
          <tr v-if="addingNew">
            <td class="px-6 py-4">
              <input type="text" v-model="newSubscriptionMode.name" class="border border-gray-300 px-4 py-2 rounded-full w-full focus:ring focus:ring-indigo-300 focus:border-indigo-500" placeholder="Enter mode name" />
            </td>
            <td class="px-6 py-4">
              <button class="bg-indigo-600 text-white px-5 py-2 rounded-full shadow-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-400 mr-2" @click="saveNewSubscriptionMode">Save</button>
              <button class="bg-gray-500 text-white px-5 py-2 rounded-full shadow-md hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-300" @click="cancelNewSubscriptionMode">Cancel</button>
            </td>
          </tr>

          <!-- Existing Modes Rows -->
          <tr v-for="mode in subscriptionModes" :key="mode._id" class="hover:bg-gray-50 transition duration-150">
            <template v-if="editMode === mode._id">
              <td class="px-6 py-4">
                <input type="text" v-model="editSubscriptionMode.name" class="border border-gray-300 px-4 py-2 rounded-full w-full focus:ring focus:ring-indigo-300 focus:border-indigo-500" />
              </td>
              <td class="px-6 py-4">
                <button class="bg-indigo-600 text-white px-5 py-2 rounded-full shadow-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-400 mr-2" @click="updateSubscriptionMode(mode._id)">Save</button>
                <button class="bg-gray-500 text-white px-5 py-2 rounded-full shadow-md hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-300" @click="cancelEdit">Cancel</button>
              </td>
            </template>
            <template v-else>
              <td class="px-6 py-4 text-md font-semibold text-gray-700 font-sans">{{ mode.name }}</td>
              <td class="px-6 py-4 flex items-center space-x-3">
                <button class="bg-yellow-500 text-white px-5 py-2 rounded-full shadow-md hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-400" @click="editSubscriptionModeFunc(mode)">Edit</button>
                <button class="bg-red-500 text-white px-5 py-2 rounded-full shadow-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-400" @click="showDeleteModal(mode._id)">Delete</button>
              </td>
            </template>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Add New Mode Button -->
    <div class="mt-6">
      <button class="bg-teal-600 text-white px-6 py-3 rounded-full shadow-md hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-teal-400" @click="startAddingNew">Add New Mode</button>
    </div>

    <!-- Confirmation Modal -->
    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscription mode?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriptionMode"
    />
  </div>
</template>

<script>
import subscriptionModeService from '../services/subscriptionModeService';
import ConfirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    ConfirmationModal
  },
  data() {
    return {
      subscriptionModes: [],
      addingNew: false,
      editMode: null,
      showConfirmationModal: false,
      modeToDelete: null,
      newSubscriptionMode: {
        name: ''
      },
      editSubscriptionMode: {
        name: ''
      }
    };
  },
  created() {
    this.loadSubscriptionModes();
  },
  methods: {
    loadSubscriptionModes() {
      subscriptionModeService.getSubscriptionModes().then(response => {
        this.subscriptionModes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription modes!", error);
      });
    },
    startAddingNew() {
      this.addingNew = true;
      this.resetNewSubscriptionMode();
    },
    cancelNewSubscriptionMode() {
      this.addingNew = false;
    },
    resetNewSubscriptionMode() {
      this.newSubscriptionMode = {
        name: ''
      };
    },
    saveNewSubscriptionMode() {
      subscriptionModeService.createSubscriptionMode(this.newSubscriptionMode).then(() => {
        this.loadSubscriptionModes();
        this.addingNew = false;
      }).catch(error => {
        console.error("There was an error saving the subscription mode!", error);
      });
    },
    editSubscriptionModeFunc(mode) {
      this.editMode = mode._id;
      this.editSubscriptionMode = { ...mode };
    },
    cancelEdit() {
      this.editMode = null;
    },
    updateSubscriptionMode(id) {
      subscriptionModeService.updateSubscriptionMode(id, this.editSubscriptionMode).then(() => {
        this.loadSubscriptionModes();
        this.editMode = null;
      }).catch(error => {
        console.error("There was an error updating the subscription mode!", error);
      });
    },
    showDeleteModal(id) {
      this.modeToDelete = id;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
      this.modeToDelete = null;
    },
    deleteSubscriptionMode() {
      subscriptionModeService.deleteSubscriptionMode(this.modeToDelete).then(() => {
        this.loadSubscriptionModes();
        this.hideDeleteModal();
      }).catch(error => {
        console.error("There was an error deleting the subscription mode!", error);
      });
    }
  }
};
</script>

<style scoped>
/* Add custom styles for smooth hover effects and modern design */
</style>
