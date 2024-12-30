<template>
  <div class="container mx-auto mt-10 px-6">
    <h2 class="text-3xl font-semibold mb-6 text-gray-800">Subscriber Types</h2>

    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-6">
      <ol class="flex space-x-2 text-sm text-gray-600">
        <li>
          <router-link to="/HomePage" class="text-blue-600 hover:underline">Home</router-link>
        </li>
        <li><span>/</span></li>
        <li class="text-gray-500" aria-current="page">Subscriber Types</li>
      </ol>
    </nav>

    <!-- Subscriber Types Table -->
    <div class="bg-white shadow-md rounded-lg overflow-hidden">
      <table class="min-w-full bg-white divide-y divide-gray-200">
        <thead class="bg-gray-100">
          <tr>
            <th class="px-6 py-4 text-left text-sm font-medium text-gray-700 uppercase tracking-wider">Name</th>
            <th class="px-6 py-4 text-left text-sm font-medium text-gray-700 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <!-- Add New Type Row -->
          <tr v-if="addingNew">
            <td class="px-6 py-4">
              <input type="text" v-model="newSubscriberType.name" class="border border-gray-300 px-3 py-2 rounded-md w-full focus:ring focus:ring-blue-200" placeholder="Enter type name" />
            </td>
            <td class="px-6 py-4 flex space-x-2">
              <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 transition focus:outline-none focus:ring-2 focus:ring-blue-500" @click="saveNewSubscriberType">Save</button>
              <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 transition focus:outline-none focus:ring-2 focus:ring-gray-500" @click="cancelNewSubscriberType">Cancel</button>
            </td>
          </tr>

          <!-- Existing Types Rows -->
          <tr v-for="type in subscriberTypes" :key="type._id" class="hover:bg-gray-50 transition">
            <template v-if="editMode === type._id">
              <td class="px-6 py-4">
                <input type="text" v-model="editSubscriberType.name" class="border border-gray-300 px-3 py-2 rounded-md w-full focus:ring focus:ring-blue-200" />
              </td>
              <td class="px-6 py-4 flex space-x-2">
                <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 transition focus:outline-none focus:ring-2 focus:ring-blue-500" @click="updateSubscriberType(type._id)">Save</button>
                <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 transition focus:outline-none focus:ring-2 focus:ring-gray-500" @click="cancelEdit">Cancel</button>
              </td>
            </template>
            <template v-else>
              <td class="px-6 py-4 text-md font-semibold text-gray-700 font-sans">{{ type.name }}</td>
              <td class="px-6 py-4 flex space-x-2">
                <button class="bg-yellow-500 text-white px-4 py-2 rounded-md shadow-md hover:bg-yellow-600 transition focus:outline-none focus:ring-2 focus:ring-yellow-400" @click="editSubscriberTypeFunc(type)">Edit</button>
                <button class="bg-red-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-red-700 transition focus:outline-none focus:ring-2 focus:ring-red-500" @click="showDeleteModal(type._id)">Delete</button>
              </td>
            </template>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Add New Type Button -->
    <button class="bg-green-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 mt-5 transition" @click="startAddingNew">Add New Type</button>

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
/* Add any additional styles here */
</style>
