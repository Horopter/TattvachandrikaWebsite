<template>
  <div class="container mx-auto mt-5 px-4">
    <h2 class="text-2xl font-bold mb-4">Subscription Languages</h2>

    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-4">
      <ol class="flex space-x-2 text-gray-700">
        <li>
          <router-link to="/" class="text-blue-600 hover:text-blue-800">Home</router-link>
        </li>
        <li>
          <span>/</span>
        </li>
        <li class="text-gray-500" aria-current="page">Subscription Languages</li>
      </ol>
    </nav>

    <!-- Subscription Languages Table -->
    <table class="min-w-full bg-white divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <!-- Add New Language Row -->
        <tr v-if="addingNew">
          <td class="px-6 py-4">
            <input type="text" v-model="newSubscriptionLanguage.name" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
          </td>
          <td class="px-6 py-4">
            <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2" @click="saveNewSubscriptionLanguage">Save</button>
            <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="cancelNewSubscriptionLanguage">Cancel</button>
          </td>
        </tr>

        <!-- Existing Languages Rows -->
        <tr v-for="language in subscriptionLanguages" :key="language._id">
          <template v-if="editMode === language._id">
            <td class="px-6 py-4">
              <input type="text" v-model="editSubscriptionLanguage.name" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
            </td>
            <td class="px-6 py-4">
              <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 mr-2" @click="updateSubscriptionLanguage(language._id)">Save</button>
              <button class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md shadow-md hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-500" @click="cancelEdit">Cancel</button>
            </td>
          </template>
          <template v-else>
            <td class="px-6 py-4 text-sm text-gray-900">{{ language.name }}</td>
            <td class="px-6 py-4">
              <button class="bg-yellow-500 text-white px-4 py-2 rounded-md shadow-md hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-400 mr-2" @click="editSubscriptionLanguageFunc(language)">Edit</button>
              <button class="bg-red-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500" @click="showDeleteModal(language._id)">Delete</button>
            </td>
          </template>
        </tr>
      </tbody>
    </table>

    <!-- Add New Language Button -->
    <button class="bg-green-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 mt-3" @click="startAddingNew">Add New Language</button>

    <!-- Confirmation Modal -->
    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscription language?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriptionLanguage"
    />
  </div>
</template>

<script>
import subscriptionLanguageService from '../services/subscriptionLanguageService';
import ConfirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    ConfirmationModal
  },
  data() {
    return {
      subscriptionLanguages: [],
      addingNew: false,
      editMode: null,
      showConfirmationModal: false,
      languageToDelete: null,
      newSubscriptionLanguage: {
        name: ''
      },
      editSubscriptionLanguage: {
        name: ''
      }
    };
  },
  created() {
    this.loadSubscriptionLanguages();
  },
  methods: {
    loadSubscriptionLanguages() {
      subscriptionLanguageService.getSubscriptionLanguages().then(response => {
        this.subscriptionLanguages = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription languages!", error);
      });
    },
    startAddingNew() {
      this.addingNew = true;
      this.resetNewSubscriptionLanguage();
    },
    cancelNewSubscriptionLanguage() {
      this.addingNew = false;
    },
    resetNewSubscriptionLanguage() {
      this.newSubscriptionLanguage = {
        name: ''
      };
    },
    saveNewSubscriptionLanguage() {
      subscriptionLanguageService.createSubscriptionLanguage(this.newSubscriptionLanguage).then(() => {
        this.loadSubscriptionLanguages();
        this.addingNew = false;
      }).catch(error => {
        console.error("There was an error saving the subscription language!", error);
      });
    },
    editSubscriptionLanguageFunc(language) {
      this.editMode = language._id;
      this.editSubscriptionLanguage = { ...language };
    },
    cancelEdit() {
      this.editMode = null;
    },
    updateSubscriptionLanguage(id) {
      subscriptionLanguageService.updateSubscriptionLanguage(id, this.editSubscriptionLanguage).then(() => {
        this.loadSubscriptionLanguages();
        this.editMode = null;
      }).catch(error => {
        console.error("There was an error updating the subscription language!", error);
      });
    },
    showDeleteModal(id) {
      this.languageToDelete = id;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
      this.languageToDelete = null;
    },
    deleteSubscriptionLanguage() {
      subscriptionLanguageService.deleteSubscriptionLanguage(this.languageToDelete).then(() => {
        this.loadSubscriptionLanguages();
        this.hideDeleteModal();
      }).catch(error => {
        console.error("There was an error deleting the subscription language!", error);
      });
    }
  }
};
</script>

<style scoped>
/* Add custom styles here if needed */
</style>
