define([],
function() {
    
    /*
    var dummy_config = {
        entity_name : 
        //string = key of this object in all_config, name of objectstore in IDB
        //for - accessing this object 
        
        'rest_api_url': '/coco/api/v2/village/',
        //string - the rest url for this entity
    
        'dashboard_display': {
            listing: false,         //whether to provide listing option for this entity on dashboard
            add: false              //whether to provide add option for this entity on dashboard
        },
    
        -----------------------------------Listing configs---------------------------------
        page_header: 'Village',  
        //string = The name that needs to shown in headers 

        list_table_header_template: 'village_table_template',  
        //HTML template - The id of template used as coloumn headers in list page

        list_table_row_template: 'village_list_item_template',  
        //HTML template - The id of template used to create rows of list table. 
        //This template is passed the model json.
        -----------------------------------------------------------------------------------
    
        ----------------------------------Form configs-------------------------------------
        foreign_entities: {
            f_entity_name:{         //the entity_name of foreign element
                attribute_name:{    //the attribute name of this foreign element in json
                    
                    'placeholder': 'string - the id of element in form's html where the dropdown of this f_entity is inserted',
                    
                    'name_field': 'string - the attribute name in f_entity's json which needs to be shown in its dropdown',
                    
                    'dependency': [{    // whether this elements's dropdown depends on value of other form elements
                        'source_form_element': 'village',   // attribute name of source element in json
                        'dep_attr': 'village'   //the attribute name in json of dependent f_entity which refers to source f_entity
                        'src_attr' : //to compare dep_attr of dependent element with a particular attribute in source f_entity
                    }],
                    
                    'filter': { //whether to filter the objects of foreign entity before rendering into dropdown
                        attr: 'group',  //the attribute name in f_entity's json to filter on
                        value: null     //desired value of the attr
                    },
    
                    id_field: "person_id", // the name of id field for this f_entity in denormalised json                         
                }
            },
    
            f_entity_name:{         //the entity_name of foreign element
                attribute_name:{    //the attribute name of this foreign element in json
                    
                    'dependency': [{    // whether this elements's dropdown depends on value of other form elements
                        'source_form_element': 'village',   // attribute name of source element in json
                        'dep_attr': 'village'   //the attribute name in json of dependent f_entity which refers to source f_entity
                    }],

                    id_field: "person_id", // the name of id field for this f_entity in denormalised json     

                    //would not use options template to render its objects - would use the specfied template    
                    // won't be denormalised, wud be converted offline to online, 
                    //any field to be denormalised or converted offline to online can be declared - 
                    //this shd be clubbed and put as foreign entity of expanded.   
                    'expanded': { 
                        template: 'person_pma_template', // the template to use instead of options
                        placeholder: 'pmas',    // the id of placeholder in form's HTML
                        TODO: the following two should be merged and converted to same format as foreign_entities
                        denormalize: { // any field in expanded template to be denormalised     
                            "expressed_adoption_video": {
                                name_field: 'title' //used as key for name in denormalised object
                            }
                        },
                        foreign_fields: { // any more field in expanded template for offline to online conv
                            "expressed_adoption_video": {
                                entity_name: "video"  //the entity_name for this f_entity element
                            }
                        },
                        extra_fields: ["expressed_question", "interested", "expressed_adoption_video"]
                    }
                }
            }
        },    
        //object - describes the foreign keys in the json of this entity's model.
        //To convert between online offline namespaces, denormalize-normalize json    
    
        inline: {
            'entity': 'person',     //entity name of inline
    
            'default_num_rows': 10,         //default num of rows to show
    
            "template": "person_inline",    //id of template used to render inline
            //Include any jquery validation desired inside html of rows 
            //TODO: need to explain the <%index%> tags required in inlines
    
            "foreign_attribute": {
                'host_attribute': ["id", "group_name"],
                'inline_attribute': "group"
            },
            "header": "person_inline_header",
            'borrow_attributes': [{
                'host_attribute': 'village',
                'inline_attribute': 'village'
            }]
        },      
        //object - describes inlines to be included in this entity's form

        bulk:{},     
        //object - if multiple objects of this entity type can be saved through its add form, describe configs of object 
        ------------------------------------------------------------------------------------
    }
    */
    
    // //This template would be passed the json of inline model and shall produce the desired row
//     TODO: maybe instead of relying on users to use templating lang we should fill the rows ourselves in js code, like we are doing in form!

    var country_configs = {
        'page_header': 'Country',
        'add_template_name': 'country_add_edit_template',
        'edit_template_name': 'country_add_edit_template',
        'rest_api_url': '/api/v1/country/',
        'list_elements': [{'element':'id'},{'header':'Name','element':'country_name'}],
        'entity_name': 'country',
        'sort_field': 'country_name',
        'form_field_validation': {
            ignore: [],
            rules: {
                country_name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    // allowedChar: true
                }
            },
            messages: {
                country_name: {
                    required: 'Country name is required',
                    minlength: 'Country name should contain at least 2 characters',
                    maxlength: 'Country name should contain at most 100 characters',
                }
            },

            highlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .addClass("error");

            },
            unhighlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .removeClass("error");

            },
            errorElement: "span",
            errorClass: "help-inline red-color",
            errorPlacement: function(label, element) {
                element.parent().append(label);
            }
        }
    };
    
    var state_configs = {
        'page_header': 'State',
        'add_template_name': 'state_add_edit_template',
        'edit_template_name': 'state_add_edit_template',
        'rest_api_url': '/api/v1/state/',
        'list_elements': [{'element':'id'},{'header':'Name','element':'state_name'}],
        'entity_name': 'state',
        'foreign_entities': {
            country: {
                country :{
                    placeholder : 'id_country',
                    name_field : 'country_name' 
                }
            }
        },
        'sort_field': 'state_name',
        'form_field_validation': {
            ignore: [],
            rules: {
                state_name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    // allowedChar: true
                },
                country: "required",
            },
            messages: {
                state_name: {
                    required: 'State name is required',
                    minlength: 'State name should contain at least 2 characters',
                    maxlength: 'State name should contain at most 100 characters',
                },
                country: "Country is required"
            },

            highlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .addClass("error");

            },
            unhighlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .removeClass("error");

            },
            errorElement: "span",
            errorClass: "help-inline red-color",
            errorPlacement: function(label, element) {
                element.parent().append(label);
            }
        }
    };
    
    var district_configs = {
        'page_header': 'District',
        'add_template_name': 'district_add_edit_template',
        'edit_template_name': 'district_add_edit_template',
            'rest_api_url': '/api/v1/district/',
            'list_elements': [{'element':'id'},{'header':'Name','element':'district_name'}],
            'entity_name': 'district',
            'foreign_entities': {
                state: {
                    state: {
                        placeholder : 'id_state',
                        name_field : 'state_name' 
                    }
                }
            },
        'sort_field': 'district_name',
        'form_field_validation': {
            ignore: [],
            rules: {
                district_name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    // allowedChar: true
                },
                state: "required",
            },
            messages: {
                district_name: {
                    required: 'District name is required',
                    minlength: 'District name should contain at least 2 characters',
                    maxlength: 'District name should contain at most 100 characters',
                },
                state: "State is required"
            },

            highlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .addClass("error");

            },
            unhighlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .removeClass("error");

            },
            errorElement: "span",
            errorClass: "help-inline red-color",
            errorPlacement: function(label, element) {
                element.parent().append(label);
            }
        }
        };
    
    var block_configs = {
        'page_header': 'Block',
        'add_template_name': 'block_add_edit_template',
        'edit_template_name': 'block_add_edit_template',
        'rest_api_url': '/api/v1/block/',
        'list_elements': [{'element':'id'},{'header':'Name','element':'block_name'}],
        'entity_name': 'block',
        'foreign_entities': {
            district: {
                district: {
                    placeholder : 'id_district',
                    name_field : 'district_name' 
                    }
                }
            },
         'sort_field': 'block_name',
         'form_field_validation': {
             ignore: [],
             rules: {
                 block_name: {
                     required: true,
                     minlength: 2,
                     maxlength: 100,
                     // allowedChar: true
                 },
                 district: "required",
             },
             messages: {
                 block_name: {
                     required: 'Block name is required',
                     minlength: 'Block name should contain at least 2 characters',
                     maxlength: 'Block name should contain at most 100 characters',
                 },
                 district: "District is required"
             },

             highlight: function(element, errorClass, validClass) {
                 $(element)
                     .parent('div')
                     .parent('div')
                     .addClass("error");

             },
             unhighlight: function(element, errorClass, validClass) {
                 $(element)
                     .parent('div')
                     .parent('div')
                     .removeClass("error");

             },
             errorElement: "span",
             errorClass: "help-inline red-color",
             errorPlacement: function(label, element) {
                 element.parent().append(label);
             }
         }
    };
    
    var sublocation_configs = {
        'page_header': 'Sublocation',
        'add_template_name': 'sublocation_add_edit_template',
        'edit_template_name': 'sublocation_add_edit_template',
        'rest_api_url': '/api/v1/sublocation/',
        'list_elements': [{'element':'id'},{'header':'Name','element':'sublocation_name'}],
        'entity_name': 'sublocation',
        'foreign_entities': {
            block: {
                block: {
                    placeholder : 'id_block',
                    name_field : 'block_name' 
                    }
                }
            },
         'unique_together_fields': ['sublocation_name', 'block.id'],
         'sort_field': 'sublocation_name',
         'form_field_validation': {
             ignore: [],
             rules: {
                 sublocation_name: {
                     required: true,
                     minlength: 2,
                     maxlength: 100,
                     // allowedChar: true
                 },
                 block: "required",
             },
             messages: {
                 sublocation_name: {
                     required: 'Sub Location name is required',
                     minlength: 'Sub Location name should contain at least 2 characters',
                     maxlength: 'Sub Location name should contain at most 100 characters',
                 },
                 block: "Block is required"
             },

             highlight: function(element, errorClass, validClass) {
                 $(element)
                     .parent('div')
                     .parent('div')
                     .addClass("error");

             },
             unhighlight: function(element, errorClass, validClass) {
                 $(element)
                     .parent('div')
                     .parent('div')
                     .removeClass("error");

             },
             errorElement: "span",
             errorClass: "help-inline red-color",
             errorPlacement: function(label, element) {
                 element.parent().append(label);
             }
         }
    };
    
    var village_configs = {
        'page_header': 'Village',
        'add_template_name': 'village_add_edit_template',
        'edit_template_name': 'vilage_add_edit_template',
        'rest_api_url': '/api/v1/village/',
        'list_elements': [{'element':'id'},{'header':'Name','element':'village_name'}],
        'entity_name': 'village',
        'foreign_entities': {
            sublocation: {
                sublocation: {
                    placeholder : 'id_sublocation',
                    name_field : 'sublocation_name' 
                }
            }
        },
        'unique_together_fields': ['village_name', 'sublocation.id'],
        'sort_field': 'village_name',
        'form_field_validation': {
            ignore: [],
            rules: {
                village_name: {
                    required: true,
                    minlength: 2,
                    maxlength: 100,
                    // allowedChar: true
                },
                sublocation: "required",
            },
            messages: {
                village_name: {
                    required: 'Village name is required',
                    minlength: 'Village name should contain at least 2 characters',
                    maxlength: 'Village name should contain at most 100 characters',
                },
                sublocation: "Sub Location is required"
            },

            highlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .addClass("error");

            },
            unhighlight: function(element, errorClass, validClass) {
                $(element)
                    .parent('div')
                    .parent('div')
                    .removeClass("error");

            },
            errorElement: "span",
            errorClass: "help-inline red-color",
            errorPlacement: function(label, element) {
                element.parent().append(label);
            }
        }
    };

    var person_configs = {
            'page_header': 'Person',
            'add_template_name': 'person_add_edit_template',
            'edit_template_name': 'person_add_edit_template',
            'list_elements': [{'element':'id'},{'element':'person_name'},{'element':'spouse_name'},{'element':'village.village_name'}],
            'rest_api_url': '/api/v1/person/',
            'entity_name': 'person',
            'foreign_entities': {
                'village': {
                    'village': {
                        'placeholder': 'id_village',
                        'name_field': 'village_name'
                    }
                }
            },
            'unique_together_fields': ['person_name', 'spouse_name', 'village.id'],
            'sort_field': 'person_name',
            'form_field_validation': {
                ignore: [],
                rules: {
                    person_name: {
                        required: true,
                        minlength: 2,
                        maxlength: 100,
                        // allowedChar:true
                    },

                    spouse_name: {
                        required: true,
                        minlength: 2,
                        maxlength: 100,
                        // allowedChar:true
                    },
                    voter_card_number:{
                        required: true,
                        minlength: 2,
                    },
                    no_of_adults:{
                        required: true,
                        digits: true,
                    },
                    no_of_children:{
                        required: true,
                        digits: true,
                    },
                    house_hold_per_capita_income:{
                        required: true,
                        digits: true,
                    },
                    phone_no: {
                        digits: true,
                        maxlength: 10
                    },
                    village: {
                        required: true
                    }
                },
                messages: {
                    person_name: {
                        required: 'Person name is required',
                        minlength: 'Person name  should contain at least 2 characters',
                        maxlength: 'Person Name should contain at most 100 characters',
                        allowedChar: 'Person name should contain only english and local language characters'
                    },
                    father_name: {
                        required: "Father's name is required",
                        minlength: "Father's name should contain at least 2 characters",
                        maxlength: "Father's name should contain at most 100 characters",
                        allowedChar: "Father's name should contain only english and local language characters"
                    },
                    phone_number_person: {
                        digits: 'Phone number should contain digits only',
                        maxlength: "Phone number should not contain more than 10 digits"
                    },
                    village: {
                        required: "Village is required"
                    }
                },

                highlight: function(element, errorClass, validClass) {
                    $(element)
                        .parent('div')
                        .parent('div')
                        .addClass("error");

                },
                unhighlight: function(element, errorClass, validClass) {
                    $(element)
                        .parent('div')
                        .parent('div')
                        .removeClass("error");

                },
                errorElement: "span",
                errorClass: "help-inline red-color",
                errorPlacement: function(label, element) {
                    element.parent().append(label);
                }
            }

        };
    var cluster_configs = {
            'page_header': 'Cluster',
            'add_template_name': 'cluster_add_edit_template',
            'edit_template_name': 'cluster_add_edit_template',
            'rest_api_url': '/api/v1/cluster/',
            'list_elements': [{'element':'id'},{'header':'Name','element':'cluster_name'}],
            'entity_name': 'cluster',
            'foreign_entities': {
                village: {
                    village: {
                        placeholder : 'id_village',
                        name_field : 'village_name' 
                        }
                    }
                },
             'sort_field': 'cluster_name'
        };
    
    var shgbaseline_configs = {
            'page_header': 'SHGBaseLine',
            'add_template_name': 'shgbaseline_add_edit_template',
            'edit_template_name': 'shgbaseline_add_edit_template',
            'rest_api_url': '/api/v1/shgbaseline/',
            'list_elements': [{'element':'id'},{'header':'Name','element':'group_name'}],
            'entity_name': 'shgbaseline',
            'foreign_entities': {
                cluster: {
                    cluster: {
                        placeholder : 'id_cluster',
                        name_field : 'cluster_name' 
                        }
                    }
                },
             'sort_field': 'group_name'
        };
    
    var shgprogram_configs = {
            'page_header': 'SHGProgram',
            'add_template_name': 'shgprogram_add_edit_template',
            'edit_template_name': 'shgprogram_add_edit_template',
            'rest_api_url': '/api/v1/shgprogram/',
            'list_elements': [{'element':'id'},{'header':'Name','element':'group_name'}],
            'entity_name': 'shgbaseline',
            'foreign_entities': {
                cluster: {
                    cluster: {
                        placeholder : 'id_cluster',
                        name_field : 'cluster_name' 
                        }
                    }
                },
             'sort_field': 'group_name'
        };
    
    var loantype_configs = {
            'page_header': 'LoanType',
            'add_template_name': 'loantype_add_edit_template',
            'edit_template_name': 'loantype_add_edit_template',
            'rest_api_url': '/api/v1/loantype/',
            'list_elements': [{'element':'id'},{'header':'Name','element':'type_name'}],
            'entity_name': 'loantype',
            'sort_field': 'type_name'
        };
    
    var loansubtype_configs = {
            'page_header': 'LoanSubType',
            'add_template_name': 'loansubtype_add_edit_template',
            'edit_template_name': 'loansubtype_add_edit_template',
            'rest_api_url': '/api/v1/loansubtype/',
            'list_elements': [{'element':'id'},{'header':'Name','element':'subtype_name'}],
            'entity_name': 'loansubtype',
            'foreign_entities': {
                'loantype': {
                    "type": {
                        'placeholder' : 'id_type',
                        'name_field' : 'type_name' 
                        }
                    }
                },
             'sort_field': 'subtype_name'
        };
    
    var loan_configs = {
            'page_header': 'Loan',
            'add_template_name': 'loan_add_edit_template',
            'edit_template_name': 'loan_add_edit_template',
            'rest_api_url': '/api/v1/loan/',
            'list_elements': [{'element':'id'},{'header':'Name','element':'loantype.type_name'}],
            'entity_name': 'loan',
            'foreign_entities': {
                'loantype': {
                    "type": {
                        'placeholder' : 'id_type',
                        'name_field' : 'type_name' 
                        }
                    },
                'loansubtype': {
                    "subtype":{
                        'placeholder' : 'id_subtype',
                        'name_field' : 'subtype_name',
                        'dependency': [{
                            'source_form_element': 'type',
                            'dep_attr': 'type'
                        }]
                        }
                    }
                }
        };

    var expectedreceipt_configs = {
            'page_header': 'ExpectedReceipt',
            'add_template_name': 'expectedreceipt_add_edit_template',
            'edit_template_name': 'expectedreceipt_add_edit_template',
            'rest_api_url': '/api/v1/expectedreceipt/',
            'list_elements': [{'element':'id'},{'header':'Name','element':'expected_savings'}],
            'entity_name': 'expectedreceipt',
        };
    
    var actualreceipt_configs = {
            'page_header': 'ActualReceipt',
            'add_template_name': 'actualreceipt_add_edit_template',
            'edit_template_name': 'actualreceipt_add_edit_template',
            'rest_api_url': '/api/v1/actualreceipt/',
            'list_elements': [{'element':'id'},{'header':'Name','element':'regular_saving'}],
            'entity_name': 'actualreceipt',
        };
    var misc = {
            download_chunk_size: 2000,
            background_download_interval: 5 * 60 * 1000,
            inc_download_url: "/get_log/",
            afterFullDownload: function(start_time, download_status){
                return saveTimeTaken();
                function saveTimeTaken(){
                    var record_endpoint = "/coco/record_full_download_time/"; 
                    return $.post(record_endpoint, {
                        start_time : start_time,
                        end_time : new Date().toJSON().replace("Z", "")
                    })    
                }
            },
            reset_database_check_url: '/coco/reset_database_check/',
            onLogin: function(Offline, Auth){
                getLastDownloadTimestamp()
                    .done(function(timestamp){
                        askServer(timestamp);
                    });
                var that = this;    
                function askServer(timestamp){
                    $.get(that.reset_database_check_url,{
                        lastdownloadtimestamp: timestamp
                    })
                        .done(function(resp){
                            console.log(resp);
                            if(resp=="1")
                            {
                                alert("Your database will be redownloaded because of some changes in data.");
                                Offline.reset_database();
                            }
                        });
                }   
                function getLastDownloadTimestamp()
                {
                    var dfd = new $.Deferred();
                    Offline.fetch_object("meta_data", "key", "last_full_download_start")
                        .done(function(model){
                            dfd.resolve(model.get("timestamp"));
                        })
                        .fail(function(model, error){
                        
                        });
                    return dfd;    
                } 
            }
        };

    return {
        country: country_configs,
        state: state_configs,
        district: district_configs,
        block: block_configs,
        sublocation: sublocation_configs,
        village: village_configs,
        person: person_configs,
        cluster: cluster_configs,
        shgbaseline: shgbaseline_configs,
        loantype: loantype_configs,
        loansubtype: loansubtype_configs,
        loan: loan_configs,
        expectedreceipt: expectedreceipt_configs,
        actualreceipt: actualreceipt_configs,
        misc: misc
    }

});
