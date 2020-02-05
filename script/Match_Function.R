# function that gets all the matching wcsp entries for a given species names (i) in the dataframe (phylo)
# requires separate lists for wcsp species and infraspecific taxa 

get_matches <- function(i, dat, wcsp_species, wcsp_infra){
  
  # initialize search for this tip label
  
  # split tip label by underscores
  tip <- strsplit(phylo$tip.label[i], "_")[[1]]
  
  # initialize vector to receive matching checklist ids
  matches <- c()
  
  # look for infraspecific taxa if enough information is available
  if(length(tip)>=4){
    #look for matches in infraspecific taxa (keeping all matches) and find the corresponding accepted species
    for(match in as.vector(wcsp_infra[wcsp_infra$genus == tip[1] & wcsp_infra$species == tip[2] & wcsp_infra$infraspecific_rank == gsub("\\.", "", tip[3]) & wcsp_infra$infraspecific_epithet == tip[4],"accepted_name_id"])){
      matches <- c(matches, as.vector(wcsp_species[wcsp_species$genus == as.vector(wcsp_infra[match,"genus"]) & wcsp_species$species == as.vector(wcsp_infra[match,"species"]) & wcsp_species$taxon_status_description == "Accepted", "checklist_id"]))
    }
  }
  
  # if there is no information on infraspecific taxa, or match at infraspecific level, move on to species level search
  if(length(matches)==0){
    # look for matches in species (keeping all matches) and find the corresponding accepted species in cases where a synonym of an ifrasp. taxon is hit
    # e.g. Macaranga schleinitziana (wcs-116515) is synonym of Macaranga involucrata var. involucrata (wcs-116515)
    for(match in as.vector(wcsp_species[wcsp_species$genus == tip[1] & wcsp_species$species == tip[2],"accepted_name_id"])){
      if(match %in% rownames(wcsp_species)){ # if it already is a species, keep match
        matches <- c(matches, match)
      } else { # if it is an infraspecific taxon, find corresponding species
        matches <- c(matches, as.vector(wcsp_species[wcsp_species$genus == as.vector(wcsp_infra[match,"genus"]) & wcsp_species$species == as.vector(wcsp_infra[match,"species"]) & wcsp_species$taxon_status_description == "Accepted","checklist_id"]))
      }
    }
  }
  
  return(unique(matches))
  
}


