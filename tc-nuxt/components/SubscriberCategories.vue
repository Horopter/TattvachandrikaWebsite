<template>
  <div class="container mx-auto mt-5 px-4">
    <h2 class="text-2xl font-bold mb-4">Subscriber Categories</h2>

    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-4">
      <ol class="flex space-x-2 text-gray-700">
        <li>
          <router-link to="/" class="text-blue-600 hover:text-blue-800">Home</router-link>
        </li>
        <li>
          <span>/</span>
        </li>
        <li class="text-gray-500" aria-current="page">Subscriber Categories</li>
      </ol>
    </nav>

    <!-- Categories Table -->
    <table class="min-w-full bg-white divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <!-- Add New Category Row -->
        <tr v-if="addingNew">
          <td class="px-6 py-4">
            <input type="text" v-model="newSubscriberCategory.name" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
          </td>
          <td class="px-6 py-4">
            <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2" @click="saveNewSubscriberCategory">Save</button>
            <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="cancelNewSubscriberCategory">Cancel</button>
          </td>
        </tr>

        <!-- Existing Categories Rows -->
        <tr v-for="category in subscriberCategories" :key="category._id">
          <template v-if="editMode === category._id">
            <td class="px-6 py-4">
              <input type="text" v-model="editSubscriberCategory.name" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
            </td>
            <td class="px-6 py-4">
              <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2" @click="updateSubscriberCategory(category._id)">Save</button>
              <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="cancelEdit">Cancel</button>
            </td>
          </template>
          <template v-else>
            <td class="px-6 py-4 text-sm text-gray-900">{{ category.name }}</td>
            <td class="px-6 py-4 text-sm text-gray-900">
              <button class="bg-yellow-500 text-white px-4 py-2 rounded-md shadow-md hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-400 mr-2" @click="editSubscriberCategoryFunc(category)">Edit</button>
              <button class="bg-red-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500" @click="showDeleteModal(category._id)">Delete</button>
            </td>
          </template>
        </tr>
      </tbody>
    </table>

    <!-- Add New Category Button -->
    <button class="bg-green-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 mt-3" @click="startAddingNew">Add New Category</button>

    <!-- Confirmation Modal -->
    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscriber category?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriberCategory"
    />
  </div>
</template>

<script>
import subscriberCategoryService from '../services/subscriberCategoryService';
import ConfirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    ConfirmationModal
  },
  data() {
    return {
      subscriberCategories: [],
      addingNew: false,
      editMode: null,
      showConfirmationModal: false,
      categoryToDelete: null,
      newSubscriberCategory: {
        name: ''
      },
      editSubscriberCategory: {
        name: ''
      }
    };
  },
  created() {
    this.loadSubscriberCategories();
  },
  methods: {
    loadSubscriberCategories() {
      subscriberCategoryService.getSubscriberCategories().then(response => {
        this.subscriberCategories = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscriber categories!", error);
      });
    },
    startAddingNew() {
      this.addingNew = true;
      this.resetNewSubscriberCategory();
    },
    cancelNewSubscriberCategory() {
      this.addingNew = false;
    },
    resetNewSubscriberCategory() {
      this.newSubscriberCategory = {
        name: ''
      };
    },
    saveNewSubscriberCategory() {
      subscriberCategoryService.createSubscriberCategory(this.newSubscriberCategory).then(() => {
        this.loadSubscriberCategories();
        this.addingNew = false;
      }).catch(error => {
        console.error("There was an error saving the subscriber category!", error);
      });
    },
    editSubscriberCategoryFunc(category) {
      this.editMode = category._id;
      this.editSubscriberCategory = { ...category };
    },
    cancelEdit() {
      this.editMode = null;
    },
    updateSubscriberCategory(id) {
      subscriberCategoryService.updateSubscriberCategory(id, this.editSubscriberCategory).then(() => {
        this.loadSubscriberCategories();
        this.editMode = null;
      }).catch(error => {
        console.error("There was an error updating the subscriber category!", error);
      });
    },
    showDeleteModal(id) {
      this.categoryToDelete = id;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
      this.categoryToDelete = null;
    },
    deleteSubscriberCategory() {
      subscriberCategoryService.deleteSubscriberCategory(this.categoryToDelete).then(() => {
        this.loadSubscriberCategories();
        this.hideDeleteModal();
      }).catch(error => {
        console.error("There was an error deleting the subscriber category!", error);
      });
    }
  }
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>
