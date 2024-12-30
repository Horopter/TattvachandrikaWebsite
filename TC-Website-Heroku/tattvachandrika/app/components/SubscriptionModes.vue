<template>
  <div class="container mx-auto mt-5 px-4">
    <h2 class="text-2xl font-bold mb-4">Subscription Modes</h2>

    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-4">
      <ol class="flex space-x-2 text-gray-700">
        <li>
          <router-link to="/" class="text-blue-600 hover:text-blue-800">Home</router-link>
        </li>
        <li>/</li>
        <li class="text-gray-500" aria-current="page">Subscription Modes</li>
      </ol>
    </nav>

    <!-- Subscription Modes Table -->
    <table class="min-w-full bg-white divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <!-- Add New Mode Row -->
        <tr v-if="addingNew">
          <td class="px-6 py-4">
            <input type="text" v-model="newSubscriptionMode.name" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
          </td>
          <td class="px-6 py-4">
            <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2" @click="saveNewSubscriptionMode">Save</button>
            <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="cancelNewSubscriptionMode">Cancel</button>
          </td>
        </tr>

        <!-- Existing Modes Rows -->
        <tr v-for="mode in subscriptionModes" :key="mode._id">
          <template v-if="editMode === mode._id">
            <td class="px-6 py-4">
              <input type="text" v-model="editSubscriptionMode.name" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
            </td>
            <td class="px-6 py-4">
              <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2" @click="updateSubscriptionMode(mode._id)">Save</button>
              <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="cancelEdit">Cancel</button>
            </td>
          </template>
          <template v-else>
            <td class="px-6 py-4 text-sm text-gray-900">{{ mode.name }}</td>
            <td class="px-6 py-4">
              <button class="bg-yellow-500 text-white px-4 py-2 rounded-md shadow-md hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-400 mr-2" @click="editSubscriptionModeFunc(mode)">Edit</button>
              <button class="bg-red-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500" @click="showDeleteModal(mode._id)">Delete</button>
            </td>
          </template>
        </tr>
      </tbody>
    </table>

    <!-- Add New Mode Button -->
    <button class="bg-green-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 mt-3" @click="startAddingNew">Add New Mode</button>

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
/* Add your styles here if needed */
</style>
