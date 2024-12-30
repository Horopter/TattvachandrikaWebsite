<template>
  <div class="container mx-auto mt-5 px-4">
    <h2 class="text-2xl font-bold mb-4">Subscriber Types</h2>

    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-4">
      <ol class="flex space-x-2 text-gray-700">
        <li>
          <router-link to="/" class="text-blue-600 hover:text-blue-800">Home</router-link>
        </li>
        <li>
          <span>/</span>
        </li>
        <li class="text-gray-500" aria-current="page">Subscriber Types</li>
      </ol>
    </nav>

    <!-- Subscriber Types Table -->
    <table class="min-w-full bg-white divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <!-- Add New Type Row -->
        <tr v-if="addingNew">
          <td class="px-6 py-4">
            <input type="text" v-model="newSubscriberType.name" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
          </td>
          <td class="px-6 py-4">
            <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2" @click="saveNewSubscriberType">Save</button>
            <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="cancelNewSubscriberType">Cancel</button>
          </td>
        </tr>

        <!-- Existing Types Rows -->
        <tr v-for="type in subscriberTypes" :key="type._id">
          <template v-if="editMode === type._id">
            <td class="px-6 py-4">
              <input type="text" v-model="editSubscriberType.name" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
            </td>
            <td class="px-6 py-4">
              <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2" @click="updateSubscriberType(type._id)">Save</button>
              <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="cancelEdit">Cancel</button>
            </td>
          </template>
          <template v-else>
            <td class="px-6 py-4 text-sm text-gray-900">{{ type.name }}</td>
            <td class="px-6 py-4">
              <button class="bg-yellow-500 text-white px-4 py-2 rounded-md shadow-md hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-400 mr-2" @click="editSubscriberTypeFunc(type)">Edit</button>
              <button class="bg-red-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500" @click="showDeleteModal(type._id)">Delete</button>
            </td>
          </template>
        </tr>
      </tbody>
    </table>

    <!-- Add New Type Button -->
    <button class="bg-green-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 mt-3" @click="startAddingNew">Add New Type</button>

    <!-- Confirmation Modal -->
    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscriber type?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriberType"
    />
  </div>
</template>

<script>
import subscriberTypeService from '../services/subscriberTypeService';
import ConfirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    ConfirmationModal
  },
  data() {
    return {
      subscriberTypes: [],
      addingNew: false,
      editMode: null,
      showConfirmationModal: false,
      typeToDelete: null,
      newSubscriberType: {
        name: ''
      },
      editSubscriberType: {
        name: ''
      }
    };
  },
  created() {
    this.loadSubscriberTypes();
  },
  methods: {
    loadSubscriberTypes() {
      subscriberTypeService.getSubscriberTypes().then(response => {
        this.subscriberTypes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscriber types!", error);
      });
    },
    startAddingNew() {
      this.addingNew = true;
      this.resetNewSubscriberType();
    },
    cancelNewSubscriberType() {
      this.addingNew = false;
    },
    resetNewSubscriberType() {
      this.newSubscriberType = {
        name: ''
      };
    },
    saveNewSubscriberType() {
      subscriberTypeService.createSubscriberType(this.newSubscriberType).then(() => {
        this.loadSubscriberTypes();
        this.addingNew = false;
      }).catch(error => {
        console.error("There was an error saving the subscriber type!", error);
      });
    },
    editSubscriberTypeFunc(type) {
      this.editMode = type._id;
      this.editSubscriberType = { ...type };
    },
    cancelEdit() {
      this.editMode = null;
    },
    updateSubscriberType(id) {
      subscriberTypeService.updateSubscriberType(id, this.editSubscriberType).then(() => {
        this.loadSubscriberTypes();
        this.editMode = null;
      }).catch(error => {
        console.error("There was an error updating the subscriber type!", error);
      });
    },
    showDeleteModal(id) {
      this.typeToDelete = id;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
      this.typeToDelete = null;
    },
    deleteSubscriberType() {
      subscriberTypeService.deleteSubscriberType(this.typeToDelete).then(() => {
        this.loadSubscriberTypes();
        this.hideDeleteModal();
      }).catch(error => {
        console.error("There was an error deleting the subscriber type!", error);
      });
    }
  }
};
</script>

<style scoped>
/* Add custom styles here if needed */
</style>
