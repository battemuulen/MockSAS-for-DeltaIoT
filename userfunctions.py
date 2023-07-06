from scipy.stats import truncnorm
import numpy as np

def myfunction(posarg, posarg2):
    print(posarg)
    return (posarg + posarg2) / 10

def truncated_normal(lower, upper, mean, stdev):
    a, b = (lower - mean) / stdev, (upper - mean) / stdev
    return truncnorm.rvs(a, b, loc=mean, scale=stdev)

def normal(mean, stdev):
    return np.random.normal(loc=mean, scale=stdev)

def uniform(lower, upper):
    return np.random.uniform(low=lower, high=upper)

def truncate(utility):
    bounds = (0, 1)
    lower_bound, upper_bound = bounds

    if utility > upper_bound:
        utility = upper_bound
    elif utility < lower_bound:
        utility = lower_bound

    range_ = upper_bound - lower_bound
    result = float((utility - lower_bound) / range_)
    return result

# def utilitySWIM(arrival_rate, dimmer, avg_response_time, max_servers, servers):
#     OPT_REVENUE = 1.5
#     BASIC_REVENUE = 1
#     SERVER_COST = 10
#     RT_THRESH = 0.75

#     ur = arrival_rate * ((1 - dimmer) * BASIC_REVENUE + dimmer * OPT_REVENUE)
#     uc = SERVER_COST * (max_servers - servers)
#     urt = 1 - ((avg_response_time - RT_THRESH) / RT_THRESH)

#     UPPER_RT_THRESHOLD = RT_THRESH * 4
#     delta_threshold = UPPER_RT_THRESHOLD - RT_THRESH
#     UrtPosFct = (delta_threshold / RT_THRESH)

#     urt_final = None
#     if avg_response_time <= UPPER_RT_THRESHOLD:
#         urt = ((RT_THRESH - avg_response_time) / RT_THRESH)
#     else:
#         urt = ((RT_THRESH - UPPER_RT_THRESHOLD) / RT_THRESH)

#     if avg_response_time <= RT_THRESH:
#         urt_final = urt * UrtPosFct
#     else:
#         urt_final = urt

#     revenue_weight = 0.7
#     server_weight = 0.3
#     utility = urt_final * ((revenue_weight * ur) + (server_weight * uc))

#     truncated_reward = truncate(utility)
#     print(truncated_reward)
#     return truncated_reward




def utilityDeltaIoT(motes_snr, packet_loss, motes_load, number_of_motes):
    # Constants
    SNR_WEIGHT = 0.35
    PACKET_LOSS_WEIGHT = 0.2
    LOAD_WEIGHT = 0.1
    NUMBER_OF_MOTES_WEIGHT = 0.35
    
    # Calculate utilities
    snr_utility = motes_snr / 100  # Assuming SNR is in dB and normalized to a scale of 0-1
    packet_loss_utility = 1 - packet_loss  # Assuming packet loss is a proportion from 0-1
    load_utility = 1 - motes_load / number_of_motes  # Assuming motes_load is total load and we want lower load per mote

    # Calculate total utility
    utility = (SNR_WEIGHT * snr_utility + PACKET_LOSS_WEIGHT * packet_loss_utility +
               LOAD_WEIGHT * load_utility + NUMBER_OF_MOTES_WEIGHT * number_of_motes / 100)  # Assuming number_of_motes is also normalized

    # Truncate utility
    truncated_utility = truncate(utility)
    
    return truncated_utility





