<template>
  <div class="container mx-auto mt-8 px-6">
    <h2 class="text-3xl font-semibold text-gray-800 mb-6">Subscriber Categories</h2>

    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-6">
      <ol class="flex items-center space-x-2 text-sm text-gray-500">
        <li>
          <router-link to="/HomePage" class="text-blue-600 hover:text-blue-700 transition-colors">Home</router-link>
        </li>
        <li>
          <span class="text-gray-400">/</span>
        </li>
        <li aria-current="page" class="text-gray-500">Subscriber Categories</li>
      </ol>
    </nav>

    <!-- Categories Table -->
    <div class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-200 bg-white shadow-lg rounded-lg overflow-hidden">
        <thead class="bg-gray-100">
          <tr>
            <th class="px-6 py-4 text-left text-sm font-semibold text-gray-600 uppercase">Name</th>
            <th class="px-6 py-4 text-left text-sm font-semibold text-gray-600 uppercase">Actions</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <!-- Add New Category Row -->
          <tr v-if="addingNew" class="bg-gray-50">
            <td class="px-6 py-4">
              <input type="text" v-model="newSubscriberCategory.name" class="border border-gray-300 focus:ring focus:ring-blue-100 focus:border-blue-300 rounded-md w-full px-4 py-2" placeholder="New Category Name" />
            </td>
            <td class="px-6 py-4">
              <button class="bg-blue-600 text-white px-4 py-2 rounded-lg shadow hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2 transition-all" @click="saveNewSubscriberCategory">Save</button>
              <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-lg shadow hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-400 transition-all" @click="cancelNewSubscriberCategory">Cancel</button>
            </td>
          </tr>

          <!-- Existing Categories Rows -->
          <tr v-for="category in subscriberCategories" :key="category._id" class="hover:bg-gray-50 transition-colors">
            <template v-if="editMode === category._id">
              <td class="px-6 py-4">
                <input type="text" v-model="editSubscriberCategory.name" class="border border-gray-300 focus:ring focus:ring-blue-100 focus:border-blue-300 rounded-md w-full px-4 py-2" />
              </td>
              <td class="px-6 py-4">
                <button class="bg-blue-600 text-white px-4 py-2 rounded-lg shadow hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2 transition-all" @click="updateSubscriberCategory(category._id)">Save</button>
                <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-lg shadow hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-400 transition-all" @click="cancelEdit">Cancel</button>
              </td>
            </template>
            <template v-else>
              <td class="px-6 py-4 text-md font-semibold text-gray-700 font-sans">{{ category.name }}</td>
              <td class="px-6 py-4">
                <button class="bg-yellow-500 text-white px-4 py-2 rounded-lg shadow hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-400 mr-2 transition-all" @click="editSubscriberCategoryFunc(category)">Edit</button>
                <button class="bg-red-600 text-white px-4 py-2 rounded-lg shadow hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 transition-all" @click="showDeleteModal(category._id)">Delete</button>
              </td>
            </template>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Add New Category Button -->
    <button class="mt-6 bg-green-600 text-white px-4 py-2 rounded-lg shadow hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 transition-all" @click="startAddingNew">Add New Category</button>

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
/* Custom styles for better UX */
</style>
